import random
import sqlite3


class DBPars:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()


    def message_analysis(self, m):
        message_array = m.split(", ")
        for el in range(len(message_array)):
            message_array[el] = message_array[el].lower()

        recipie_dir = {}
        with self.connection:
            for el in message_array:
                res = self.cursor.execute("SELECT RECIPIE_ID FROM INGREDIENTS WHERE NAME = ?", (el,)).fetchall()
                recipie_dir[el] = res
        recipies = []
        for key in recipie_dir.keys():
            if recipie_dir[key] == [] and len(recipie_dir) == 1: return 'Мы не смогли ничего найти по Вашему запросу😰 \nПожалуйста, введите другие ингредиенты!'
            recipies.append(recipie_dir[key])

        res = set(recipies[0])
        for i in range(1, len(recipies)):
            res = res & set(recipies[i])
        result = list(res)

        if result == []: return 'Мы не смогли ничего найти по Вашему запросу😰 \nПопробуйте ввести другое сочетание ингредиентов!'

        total_recipie = int(str(random.choice(result))[1:][:-2])

        text_to_return = ''
        with self.connection:
            res = self.cursor.execute("SELECT * FROM RECIPIES WHERE ID = ?", (total_recipie,)).fetchone()
            text_to_return += res[2] + '\n\n' + 'Ингредиенты: \n' + res[1] + '\n\n' + 'Рецепт: \n' + res[3]

        return text_to_return

    def random_recipie(self):
        random_id = random.randint(0, 61565)
        text_to_return = ''
        with self.connection:
            res = self.cursor.execute("SELECT * FROM RECIPIES WHERE ID = ?", (random_id,)).fetchone()

            text_to_return += res[2] + '\n\n' + 'Ингредиенты: \n' + res[1] + '\n\n' + 'Рецепт: \n' + res[3]

        return text_to_return


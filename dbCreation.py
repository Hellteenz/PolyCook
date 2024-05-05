import sqlite3
import pandas as pd
piss = pd.read_csv("pecipes_all.csv")
piss_ing = piss.get('ingridients')
ing_amount = []
piss_pure_ing = piss.get('pure_ingridients')
pure_ing = []
piss_instructions = piss.get('instructions')
instructions = []
piss_names = piss.get('name')
names = []
for i in range(len(piss)):
    ia = piss_ing[i].replace('[','').replace(']', '').replace("'",'')
    pi = piss_pure_ing[i].replace('[','').replace(']', '').replace("'",'').split(', ')
    inst = piss_instructions[i].replace('[','').replace(']', '').replace("'", '').replace(".,", '.')
    if type(piss_names[i]) == str:
        n = piss_names[i].replace("'", '')
    if len(n) > 0 and len(ia) > 0 and len(pi) > 0 and len(inst) > 0 and type(piss_names[i]) == str:
        ing_amount.append(ia)
        pure_ing.append(pi)
        instructions.append(inst)
        names.append(n)
connection = sqlite3.connect(r"recipies.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS RECIPIES(
ID INT PRIMARY KEY,
NAME VARCHAR(244),
ING_AMOUNT VARCHAR(244),
RECIPIE VARCHAR(244))
''')
for i in range(len(names)):
    a = names[i]
    b = instructions[i]
    c = ing_amount[i]
    print(a,b,c)
    cursor.execute(f'INSERT INTO RECIPIES (ID, NAME, ING_AMOUNT, RECIPIE) VALUES ({i}, \'{c}\', \'{a}\', \'{b}\')')

cursor.execute("""SELECT * FROM recipies""")
print(cursor.fetchall())
ing_set = set()
for i in pure_ing:
    for j in i:
        ing_set.add(j.lower())
ing_set = sorted(ing_set)
print(ing_set)
cursor.execute('''
CREATE TABLE IF NOT EXISTS INGREDIENTS(
ID INT PRIMARY KEY,
NAME VARCHAR(244),
RECIPIE_ID INT)
''')
id_cnt = 0
for i in ing_set:
    for j in range(len(pure_ing)):
        if i in pure_ing[j]:
            cursor.execute(f'INSERT INTO INGREDIENTS (ID, NAME, RECIPIE_ID) VALUES ({id_cnt}, \'{i}\', {j})')
            id_cnt += 1
cursor.execute("""SELECT * FROM INGREDIENTS""")
print(cursor.fetchall())
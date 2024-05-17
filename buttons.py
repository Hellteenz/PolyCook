from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMainMenu = KeyboardButton(text='В главное меню 🍋')

btnInstruction = KeyboardButton(text='Инструкции 📝')
btnProducts = KeyboardButton(text='Поиск по продуктам 🥟')
btnRandom = KeyboardButton(text='Случайное блюдо 🍰')


mainMenuKB = [
    [btnInstruction],
    [btnProducts],
    [btnRandom]
]
mainMenu = ReplyKeyboardMarkup(keyboard=mainMenuKB)

# ------------------
btnRetry_prod = KeyboardButton(text='Другой рецепт 🔄')

productsMenuKB = [
    [btnRetry_prod],
    [btnMainMenu]
]
productsMenu = ReplyKeyboardMarkup(keyboard=productsMenuKB)


# ------------------
btnRetry_time = KeyboardButton(text='Следующий рецепт 🔄')

timeMenuKB = [
    [btnRetry_time],
    [btnMainMenu]
]
timeMenu = ReplyKeyboardMarkup(keyboard=timeMenuKB)

# ------------------
btnRetry_rand = KeyboardButton(text='Другой рецепт 🔁')

randomMenuKB = [
    [btnRetry_rand],
    [btnMainMenu]
]
randomMenu = ReplyKeyboardMarkup(keyboard=randomMenuKB)
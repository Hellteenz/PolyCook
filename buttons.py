from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMainMenu = KeyboardButton('В главное меню 🍋')

btnInstruction = KeyboardButton('Инструкции 📝')
btnProducts = KeyboardButton('Поиск по продуктам 🥟')
btnTime = KeyboardButton('Поиск по времени 🕰')
btnRandom = KeyboardButton('Случайное блюдо 🍰')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnInstruction)
mainMenu.add(btnProducts)
mainMenu.add(btnTime)
mainMenu.add(btnRandom)

# ------------------
btnRetry_prod = KeyboardButton('Другой рецепт 🔄')

productsMenu = ReplyKeyboardMarkup(resize_keyboard=True)
productsMenu.add(btnRetry_prod)
productsMenu.add(btnMainMenu)

# ------------------
btnRetry_time = KeyboardButton('Следующий рецепт 🔄')

timeMenu = ReplyKeyboardMarkup(resize_keyboard=True)
timeMenu.add(btnRetry_time)
timeMenu.add(btnMainMenu)

# ------------------
btnRetry_rand = KeyboardButton('Другой рецепт 🔁')

randomMenu = ReplyKeyboardMarkup(resize_keyboard=True)
randomMenu.add(btnRetry_rand)
randomMenu.add(btnMainMenu)
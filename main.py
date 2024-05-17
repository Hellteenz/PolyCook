import asyncio

import logging
from aiogram import types, Dispatcher, Bot
import buttons as btn
from aiogram.filters.command import Command
from parsing import DBPars

TOKEN = '7191989962:AAHbq6KLVaB3nBb_rMnqagLIM6nm77D8YQM'
bot = Bot(TOKEN)

logging.basicConfig(level=logging.INFO)
dp = Dispatcher()
pars = DBPars('C:\\Users\\1cept\\PycharmProjects\\PolyCook\\dir\\recipies.db')


async def main():
    await dp.start_polling(bot)


@dp.message(Command('start'))
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Приветствую! 👋 \nЯ - бот PolyCook, который готов помочь разнообразить Вашу кулинарную '
                           'жизнь простыми рецептами из того, что есть под рукой☺️\n\nВам достаточно ввести набор '
                           'продуктов, из которого Вы хотите получить блюдо, а я Вам сформирую интересный рецептик 🥰',
                           reply_markup=btn.mainMenu)


# обработка сообщений
@dp.message()
async def bot_message(message: types.Message):
    if message.text == 'Инструкции 📝':
        await bot.send_message(message.from_user.id, 'Функции ☀️', reply_markup=btn.mainMenu)

    elif message.text == 'Другой рецепт 🔄' or message.text == 'Поиск по продуктам 🥟':
        await bot.send_message(message.from_user.id, '🥕 Введите ингредиенты, которые Вы хотите использовать (не больше 5 🥺) : ',
                               reply_markup=btn.productsMenu)

    elif message.text == 'Другой рецепт 🔁' or message.text == 'Случайное блюдо 🍰':
        await bot.send_message(message.from_user.id, pars.random_recipie(),
                               reply_markup=btn.randomMenu)

    elif message.text == 'В главное меню 🍋':
        await bot.send_message(message.from_user.id, 'Главное меню 🍲', reply_markup=btn.mainMenu)

    else:
        ingredients = message.text
        await bot.send_message(message.from_user.id, pars.message_analysis(ingredients), reply_markup=btn.productsMenu)


if __name__ == '__main__':
    asyncio.run(main())

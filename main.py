import telebot
import time
import logging
from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor
import buttons as btn

TOKEN = ''
bot = Bot(token=TOKEN)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Приветствую! 👋 \nЯ - бот PolyCook, который готов помочь разнообразить Вашу кулинарную '
                           'жизнь простыми рецептами из того, что есть под рукой☺️\n\nВам достаточно ввести набор '
                           'продуктов, из которого Вы хотите получить блюдо, а я Вам сформирую интересный рецептик 🥰',
                           reply_markup=btn.mainMenu)


# обработка сообщений
@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == 'Инструкции 📝':
        await bot.send_message(message.from_user.id, 'Функции ☀️', reply_markup=btn.mainMenu)

    elif message.text == 'Другой рецепт 🔄' or message.text == 'Поиск по продуктам 🥟':
        await bot.send_message(message.from_user.id, 'Минутку! Мы уже готовим Ваше блюдо! 👨🏽‍🍳',
                               reply_markup=btn.productsMenu)

    elif message.text == 'Следующий рецепт 🔄' or message.text == 'Поиск по времени 🕰':
        await bot.send_message(message.from_user.id, 'Минутку! Мы уже готовим Ваше блюдо! 👨🏽‍🍳',
                               reply_markup=btn.timeMenu)

    elif message.text == 'Другой рецепт 🔁' or message.text == 'Случайное блюдо 🍰':
        await bot.send_message(message.from_user.id, 'Минутку! Мы уже готовим Ваше блюдо! 👨🏽‍🍳',
                               reply_markup=btn.randomMenu)

    elif message.text == 'В главное меню 🍋':
        await bot.send_message(message.from_user.id, 'Главное меню 🍲', reply_markup=btn.mainMenu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

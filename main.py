import telebot
import time
import logging
from aiogram import types, Dispatcher, Bot
from aiogram.utils import executor

TOKEN = '7191989962:AAHbq6KLVaB3nBb_rMnqagLIM6nm77D8YQM'
bot = Bot(token=TOKEN)
logging.basicConfig(level=logging.INFO)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboardgostart = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Инструкции 📝']])
    keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Поиск по продуктам 🥟']])
    keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Поиск по времени 🕰']])
    keyboardgostart.add(*[types.KeyboardButton(name) for name in ['Случайное блюдо 🍰']])
    await bot.send_message(message.from_user.id,
                           'Приветствую! 👋 \nЯ - бот PolyCook, который готов помочь разнообразить твою кулинарную '
                           'жизнь простыми рецептами из того, что есть под рукой☺️\nВам достаточно ввести набор '
                           'продуктов, из которого Вы хотите получить блюдо, а я Вам сформирую интересный рецептик 🥰',
                           reply_markup=keyboardgostart)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

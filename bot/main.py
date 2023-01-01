"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from buttons import button
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
API_TOKEN = '5986096208:AAE_UIcHt9m1gFhFvUtBKpvcRTRxwZzgxRI'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.",reply_markup =button)
    print(message.from_user.id)



@dp.message_handler(Text(startswith='ish beruvchi'))
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer('iltimos shu link orqali formani tolidiring, http://127.0.0.1:8000/form/')

@dp.message_handler(Text(startswith='ishchi'))
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer('iltimos shu link orqali formani tolidiring, http://127.0.0.1:8000/form/')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
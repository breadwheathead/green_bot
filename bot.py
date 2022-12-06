import logging
from aiogram import Bot
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

help_text = 'Список доступных команд:\n' \
            '/weather - прогноз погоды в локации на сегодня\n' \
            '/rate - курс доллара на текущий момент'


@dp.message_handler(commands='start')
async def start_command(message: Message):
    await message.answer('Привет!\n' + help_text)


@dp.message_handler(commands='help')
async def help_command(message: Message):
    await message.answer(help_text)


@dp.message_handler(commands='weather')
async def get_weather_command(message: Message):
    await message.answer('заглушка')


@dp.message_handler(commands='rate')
async def get_rate_command(message: Message):
    await message.answer('заглушка')


@dp.message_handler(content_types='text')
async def echo(message: Message):
    await message.reply(f'Пока что я просто повторяю любое сообщение, кроме команд: {message.text}')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

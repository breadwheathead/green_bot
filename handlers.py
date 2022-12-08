from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.dispatcher import Dispatcher
from bot_init import bot
from messages import MESSAGES
from keyboards import keyboard


async def start_command(message: Message):
    await bot.send_message(message.from_user.id, MESSAGES['welcome'].format(message.from_user.first_name), reply_markup=ReplyKeyboardRemove())


async def help_command(message: Message):
    await message.answer(MESSAGES['help'])


async def get_weather_command(message: Message):
    await message.answer('заглушка')


async def get_rate_command(message: Message):
    await message.answer('заглушка')


async def echo(message: Message):
    await message.reply(f'Пока что я просто повторяю любое сообщение, кроме команд: {message.text}')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands='start')
    dp.register_message_handler(help_command, commands='help')
    dp.register_message_handler(get_weather_command, commands='weather')
    dp.register_message_handler(get_rate_command, commands='rate')
    dp.register_message_handler(echo, content_types='text')

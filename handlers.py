from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from bot_init import bot
from config import ADMIN_ID
from messages import MESSAGES
from keyboards import keyboard


async def access_denied(message: Message):
    await message.delete()
    await message.answer('Вам отказано в доступе!')


async def start_command(message: Message):
    await bot.send_message(message.from_user.id, MESSAGES['welcome'].format(message.from_user.first_name),
                           reply_markup=keyboard)


async def help_command(message: Message):
    await message.answer(MESSAGES['help'])


async def weather_command(message: Message):
    await message.answer('заглушка')


async def rate_command(message: Message):
    await message.answer('заглушка')


async def unknown_command(message: Message):
    await message.delete()


def register_handlers(dp: Dispatcher):
    # access denied
    dp.register_message_handler(access_denied, lambda m: m.chat.id != ADMIN_ID, content_types=types.ContentTypes.ANY)

    dp.register_message_handler(start_command, commands='start')
    dp.register_message_handler(help_command, commands='help')
    dp.register_message_handler(weather_command, commands='weather')
    dp.register_message_handler(rate_command, commands='rate')
    dp.register_message_handler(unknown_command, content_types=types.ContentTypes.ANY)

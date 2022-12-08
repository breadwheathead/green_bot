from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher import Dispatcher, filters
from bot_init import bot
from messages import MESSAGES
from keyboards import reply_button, keyboard


async def callback_weather(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Тут потом будет погода')


async def callback_rate(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Тут потом будет курс доллара')


async def start_command(message: Message):
    await bot.send_message(message.from_user.id, MESSAGES['welcome'].format(message.from_user.first_name),
                           reply_markup=reply_button)


# async def help_command(message: Message):
#     await message.answer(MESSAGES['help'])


# async def weather_command(message: Message):
#     await message.answer('заглушка')
#
#
# async def rate_command(message: Message):
#     await message.answer('заглушка')


async def show_keyboard(message: Message):
    await bot.send_message(message.from_user.id, 'Вот что я могу 😊', reply_markup=keyboard)


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    # dp.register_message_handler(help_command, commands='help')
    # dp.register_message_handler(weather_command, commands='weather')
    # dp.register_message_handler(rate_command, commands='rate')
    dp.register_message_handler(show_keyboard, filters.Text(equals='Показать кнопки'))
    dp.register_callback_query_handler(callback_weather, lambda c: c.data == 'weather')
    dp.register_callback_query_handler(callback_rate, lambda c: c.data == 'rate')

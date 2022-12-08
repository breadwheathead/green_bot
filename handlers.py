from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, ContentTypes
from aiogram.dispatcher import Dispatcher, filters
from bot_init import bot
from config import ADMIN_ID
from messages import MESSAGES
from keyboards import reply_button, keyboard


async def callback_weather(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, 'Тут потом будет погода')
    await call.answer(text='Спасибо, что воспользовались ботом!', show_alert=True)


async def callback_rate(call: CallbackQuery):
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.from_user.id, 'Тут потом будет курс доллара')


async def access_denied(message: Message):
    await message.answer('Вам отказано в доступе!')


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


async def unknown_command(message: Message):
    await message.delete()


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(callback_weather, lambda c: c.data == 'weather')
    dp.register_callback_query_handler(callback_rate, lambda c: c.data == 'rate')

    '''access denied'''
    dp.register_message_handler(access_denied, lambda m: m.chat.id != ADMIN_ID, content_types=ContentTypes.ANY)

    dp.register_message_handler(start_command, commands=['start', 'help'])
    # dp.register_message_handler(help_command, commands='help')
    # dp.register_message_handler(weather_command, commands='weather')
    # dp.register_message_handler(rate_command, commands='rate')
    dp.register_message_handler(show_keyboard, filters.Text(equals='Показать кнопки'))
    dp.register_message_handler(unknown_command, content_types=ContentTypes.ANY)


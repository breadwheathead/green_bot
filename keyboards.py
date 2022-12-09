from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bottom_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
weather_btn = KeyboardButton('/weather')
rate_btn = KeyboardButton('/rate')
bottom_keyboard.add(weather_btn, rate_btn)

weather_keyboard = InlineKeyboardMarkup(row_width=2)
weather_city = InlineKeyboardButton('Указать город', callback_data='weather_city')
weather_location = InlineKeyboardButton('Отправить локацию', callback_data='weather_location')
weather_keyboard.add(weather_city, weather_location)

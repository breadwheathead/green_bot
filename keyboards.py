from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
weather_btn = KeyboardButton('/weather')
rate_btn = KeyboardButton('/rate')

keyboard.add(weather_btn, rate_btn)

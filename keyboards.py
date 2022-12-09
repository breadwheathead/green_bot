from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

bottom_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
weather_btn = KeyboardButton('/weather')
rate_btn = KeyboardButton('/rate')
bottom_keyboard.add(weather_btn, rate_btn)

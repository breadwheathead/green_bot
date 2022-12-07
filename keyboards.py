from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
weather_btn = KeyboardButton('Прогноз погоды')
rate_btn = KeyboardButton('Курс доллара')

keyboard.add(weather_btn, rate_btn)
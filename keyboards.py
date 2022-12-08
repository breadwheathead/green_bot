from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

reply_button = ReplyKeyboardMarkup(resize_keyboard=True).add('Показать кнопки')

keyboard = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True)
weather_btn = InlineKeyboardButton('Прогноз погоды ⛅', callback_data='weather')
rate_btn = InlineKeyboardButton('Курс доллара 💲', callback_data='rate')

keyboard.add(weather_btn, rate_btn)

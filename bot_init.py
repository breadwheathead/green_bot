from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config.config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher(bot)

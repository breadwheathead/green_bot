import logging
from aiogram.types import BotCommand
from aiogram.utils import executor
from bot_init import dp, bot
from handlers import register_handlers

logging.basicConfig(level=logging.INFO)

COMMANDS = [
    BotCommand('/help', 'Доступные команды'),
    BotCommand('/weather', 'Прогноз погоды в локации на сегодня'),
    BotCommand('/rate', 'Курс доллара на текущий момент')
]


async def on_startup(_):
    logging.info('Бот в работе')
    await bot.delete_my_commands()
    await bot.set_my_commands(COMMANDS)

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

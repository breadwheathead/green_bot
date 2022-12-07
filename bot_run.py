import logging
from aiogram.utils import executor
from bot_init import dp, bot

logging.basicConfig(level=logging.INFO)


async def on_startup():
    bot.delete_my_commands()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

import logging
from aiogram.utils import executor
from bot_init import dp, bot
from handlers import register_handlers

logging.basicConfig(level=logging.INFO)


async def on_startup(_):
    logging.info('Бот в работе')
    await bot.delete_my_commands()

register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

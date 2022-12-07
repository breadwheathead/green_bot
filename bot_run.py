import logging
from aiogram.utils import executor
from bot_init import dp

logging.basicConfig(level=logging.INFO)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

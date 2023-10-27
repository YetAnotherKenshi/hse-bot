import asyncio
import logging
from aiogram import Bot, Dispatcher

from aiogram.utils import executor


logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
bot = Bot(token='5684479374:AAF5LIuo1Ejjv0dxLlSzIEpdZcRoQJyuOCw')
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp
    executor.start_polling(dp, skip_updates=True)
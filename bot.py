import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.utils import executor
from aiogram.utils.executor import start_webhook
from config import USE_WEBHOOKS, BOT_TOKEN, WEBAPP_HOST, WEBAPP_PORT, WEBHOOK_PATH, WEBHOOK_URL

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def on_startup(dp):
    print('Bot started')
    await bot.set_webhook(WEBHOOK_URL)


async def on_shutdown(dp):
    await bot.delete_webhook()

if __name__ == '__main__':
    from handlers import dp

    if USE_WEBHOOKS:
        start_webhook(
            dispatcher=dp,
            webhook_path=WEBHOOK_PATH,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=WEBAPP_HOST,
            port=WEBAPP_PORT,
        )
    else:
        executor.start_polling(dp)

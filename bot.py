import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from get_pokemon import get_pokemon_info

logging.basicConfig(level=logging.INFO)

loop = asyncio.get_event_loop()
bot = Bot(token='5684479374:AAF5LIuo1Ejjv0dxLlSzIEpdZcRoQJyuOCw')
dp = Dispatcher(bot)

@dp.message_handler()
async def poke_message(message: types.Message):
    res = get_pokemon_info(message.text.strip().lower())
    if res != None:
        media = types.MediaGroup()
        media.attach_photo(res["url"], "\n".join(res["info"]))
        media.attach_photo(res["url2"])
        await bot.send_media_group(message.chat.id, media)
    else: 
        await bot.send_message(message.chat.id, "Такого покемона не существует!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
import asyncio
import uvicorn
import multiprocessing
from aiogram import Bot, Dispatcher
from newsbot.news_bot import bot_router
from configs import TELEGRAM_API_TOKEN
from main import app as api_app
bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher()
dp.include_router(bot_router)
async def run_bot():
    await dp.start_polling(bot)
def run_api():
    uvicorn.run(api_app, host="0.0.0.0", port=8000)

async def run_both():
    api_process = multiprocessing.Process(target=run_api)
    api_process.start()
    try:
        await run_bot()
    finally:
        api_process.terminate()
        api_process.join()
if __name__ == "__main__":
    asyncio.run(run_both())
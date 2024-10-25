import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router
from dotenv import load_dotenv
import os

async def main():
    load_dotenv()
    bot = Bot(os.getenv('TOKEN'))
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot is disabled")
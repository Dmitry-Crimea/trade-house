import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main
from config import TOKEN

async def main():
    await async_main()
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.error(f"Bot shutdown")

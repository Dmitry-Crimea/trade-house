import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main

logging.basicConfig(level=logging.DEBUG)


async def main():
    await async_main()
    bot = Bot(token='6862227221:AAFz0PpN0X6mZIvxY1-lv3zBofPGq_Nzv-8')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.error(f"Bot shutdown")

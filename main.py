import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import router

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token='6700364208:AAFbW5IYX-8BuYHz0-BnSw5PF5Me_2OspZU')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
      asyncio.run(main())
    except KeyboardInterrupt:
      logger.error(f"Bot shutdown")

from aiogram import Bot, Dispatcher
import asyncio

bot = Bot(token='')
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__'
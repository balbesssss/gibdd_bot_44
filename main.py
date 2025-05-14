"""Модуль для запуска"""
import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

load_dotenv(".env")
TOKEN = os.getenv('TOKEN')
BOT = Bot(token=TOKEN)
DP = Dispatcher()


async def main():
    """Запуск бота"""
    try:
        await DP.start_polling(BOT, skip_updatet=True)
    finally:
        await BOT.session.close()

if __name__ == '__main__':
    asyncio.run(main())

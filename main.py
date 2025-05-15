"""Модуль для запуска"""
import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handler import add_routers

load_dotenv(".env")
TOKEN = os.getenv('TOKEN')
BOT = Bot(token=TOKEN)
DP = Dispatcher()


async def main():
    """Запуск бота"""
    try:
        add_routers(DP)
        await DP.start_polling(BOT, skip_updatet=True)
    finally:
        await BOT.session.close()

if __name__ == '__main__':
    asyncio.run(main())

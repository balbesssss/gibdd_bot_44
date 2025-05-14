"""Модуль для запуска"""
import os
import asyncio
from aiogram import Bot,Dispatcher
from dotenv import load_dotenv
from bot.handlers.handlers import function

load_dotenv(".env")
bot=os.getenv('Bot')
bot=Bot(token=bot)
dp = Dispatcher()


async def main():
    """Запуск бота"""
    try:
        function(dp)
        await dp.start_polling(bot,skip_updatet=True)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
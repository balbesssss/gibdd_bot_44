"""подключение роутеров"""

from aiogram import Dispatcher
from .user_ban import router as user_ban


def add_routers(dp: Dispatcher):
    """Подключение роутеров"""
    dp.include_routers(user_ban)

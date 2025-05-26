"""подключение роутеров"""

from aiogram import Dispatcher
from .user_ban import router as user_ban
from .start_patrol import router as start_patrol
from .end_patrol import router as end_patrol


def add_routers(dp: Dispatcher):
    """Подключение роутеров"""
    dp.include_routers(user_ban)
    dp.include_router(start_patrol)
    dp.include_router(end_patrol)

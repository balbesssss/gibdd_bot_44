"""подключение роутеров"""

from aiogram import Dispatcher
from .add_role import router as add_role_router


def add_routers(dp: Dispatcher):
    """Подключение роутеров"""
    dp.include_routers(add_role_router)

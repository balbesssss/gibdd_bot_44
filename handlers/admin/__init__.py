"""подключение роутеров"""
from aiogram import Dispatcher
from .admin import router as admin_router


def add_routers(dp: Dispatcher):
    """Подключение роутеров"""
    dp.include_routers(
        admin_router
    )

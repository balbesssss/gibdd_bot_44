"""подключение роутеров администратора"""
from aiogram import Dispatcher
from .add_inspector import router as add_inspector_router


def add_routers(dp: Dispatcher):
    """Подключение роутеров"""
    dp.include_routers(
        add_inspector_router
    )

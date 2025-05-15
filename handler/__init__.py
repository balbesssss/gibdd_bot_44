"""подключение роутеров"""
from aiogram import Dispatcher
from start import router as start_router


def add_routers(dp: Dispatcher):
    dp.include_routers([
        start_router
    ])

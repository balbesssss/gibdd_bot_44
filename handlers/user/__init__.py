"""подключение роутеров"""

from aiogram import Dispatcher
from .start import router as start_router
from .send_message import router as send_message_router


def add_routers(dp: Dispatcher):
    """Подключение роутеров"""
    dp.include_routers(
        start_router,
        send_message_router
    )

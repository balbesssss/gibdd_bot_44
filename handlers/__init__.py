"""подключение роутеров"""

from aiogram import Dispatcher
from .user import add_routers as user_add_routers
from .admin import add_routers as admin_add_routers


def add_routers(dp: Dispatcher):
    """Подключение роутеров"""
    user_add_routers(dp)
    admin_add_routers(dp)

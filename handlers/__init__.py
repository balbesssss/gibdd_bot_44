"""подключение роутеров"""

from aiogram import Dispatcher
from .user import add_routers as user_add_routers
from .admin import add_routers as admin_add_routers
from .inspector import add_routers as inspector_add_routers


def add_routers(dp: Dispatcher):
    """Подключение роутеров"""
    admin_add_routers(dp)
    inspector_add_routers(dp)
    user_add_routers(dp)

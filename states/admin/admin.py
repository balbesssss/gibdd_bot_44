"""Состояние для добавления администратора"""
from aiogram.fsm.state import State, StatesGroup
# pylint: disable=R0903


class AddAdmin(StatesGroup):
    """Класс для описания состояния"""
    get_contact = State()

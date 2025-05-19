"""Состояние для добавления инспектора"""

from aiogram.fsm.state import State, StatesGroup

# pylint: disable=R0903


class AddInspector(StatesGroup):
    """Класс для описания состояния"""

    get_contact = State()

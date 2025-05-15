"""Состояние для добовления инспектора"""
from aiogram.fsm.state import State, StatesGroup


class AddInspector(StatesGroup):
    """Класс для описания состояния"""
    contact = State()

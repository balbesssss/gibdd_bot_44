"""Обработчик добавления инспектора администратором"""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.admin.inspector import AddInspector
from filters.admin import IsAdmin

router = Router()


@router.message(F.text() == "Добавить инспектора", IsAdmin())
async def add_inspector_start(message: Message, state: FSMContext):
    """Обработчик начала добавления инспектора"""
    await message.answer("Отправьте контакт сотрудника")
    await state.set_state(AddInspector.get_contact)

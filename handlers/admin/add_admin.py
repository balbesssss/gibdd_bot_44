"""Обработка команд Администратора"""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from filters.admin import IsAdmin
from states.admin.admin import AddAdmin

router = Router()


@router.message(F.text == "Добавить администратора", IsAdmin())
async def add_admin(message: Message, state: FSMContext):
    """Обработчик сообщения для добавления администратора"""

    await message.answer(text="Отправьте контакт сотрудника")
    await state.set_state(AddAdmin.get_contact)

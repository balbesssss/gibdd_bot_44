"""Обработчик добавления инспектора администратором"""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from states.admin.inspector import AddInspector
from filters.admin import IsAdmin
from filters.inspector import IsInspector
from database.models import User, UserRole

router = Router()


@router.message(F.text == "Добавить инспектора", IsAdmin())
async def add_inspector_start(message: Message, state: FSMContext):
    """Обработчик начала добавления инспектора"""
    await message.answer("Отправьте контакт сотрудника")
    await state.set_state(AddInspector.get_contact)


@router.message(F.contact, IsAdmin(), AddInspector.get_contact)
async def get_inspector_contact(message: Message, state: FSMContext):
    """Обработчик получения контакта инспектора"""
    contact = message.contact
    user_id = contact.user_id if contact.user_id else None

    user = User.get_or_none(User.tg_id == user_id)
    if not user:
        await message.answer("Такой сотрудник не запускал бота")
        await state.clear()
        return

    if contact.phone_number and user.phone != contact.phone_number:
        user.phone = contact.phone_number
        user.save()

    if contact.last_name and user.last_name != contact.last_name:
        user.last_name = contact.last_name
        user.save()

    if contact.first_name and user.first_name != contact.first_name:
        user.first_name = contact.first_name
        user.save()

    inspector_role = IsInspector.role

    user_role = UserRole.get_or_none(
        (UserRole.user == user) & (UserRole.role == inspector_role)
    )

    if user_role:
        await message.answer("Этому сотруднику уже выдавалась роль инспектора")
    else:
        UserRole.create(user=user, role=inspector_role)
        await message.answer("Роль Инспектора добавлена")
    await state.clear()

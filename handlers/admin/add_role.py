"""Добавление ролей"""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.types.contact import Contact
from aiogram.fsm.context import FSMContext
from states.admin.inspector import AddInspector
from states.admin.admin import AddAdmin
from filters.admin import IsAdmin
from filters.inspector import IsInspector
from database.models import Role, User, UserRole, Admin

router = Router()


@router.message(F.text == "Добавить администратора", IsAdmin())
async def add_admin_start(message: Message, state: FSMContext):
    """Обработчик начала добавления администратора"""
    await message.answer("Отправьте контакт сотрудника")
    await state.set_state(AddAdmin.get_contact)


async def add_role(contact: Contact, role: Role):
    """Добавление роли"""
    user = User.get(User.tg_id == contact.user_id)

    if contact.last_name and user.last_name != contact.last_name:
        user.last_name = contact.last_name
        user.save()

    if contact.first_name and user.first_name != contact.first_name:
        user.first_name = contact.first_name
        user.save()

    return (
        UserRole.get_or_none(
            (UserRole.user == user) & (UserRole.role == role)
        ),
        user,
    )


@router.message(F.contact, IsAdmin(), AddAdmin.get_contact)
async def get_admin_contact(message: Message, state: FSMContext):
    """Обработчик получения контакта администратора"""
    contact: Contact = message.contact
    user_role, user = await add_role(
        contact=contact,
        role=IsAdmin.role,
    )

    if user_role:
        await message.answer(
            "Этому сотруднику уже выдавалась роль администратора"
        )
    else:
        UserRole.create(user=user, role=IsAdmin.role)
        Admin.get_or_create(user=user)
        await message.answer("Роль администратора добавлена")
    await state.clear()


@router.message(F.text == "Добавить инспектора", IsAdmin())
async def add_inspector_start(message: Message, state: FSMContext):
    """Обработчик начала добавления инспектора"""
    await message.answer("Отправьте контакт сотрудника")
    await state.set_state(AddInspector.get_contact)


@router.message(F.contact, IsAdmin(), AddInspector.get_contact)
async def get_inspector_contact(message: Message, state: FSMContext):
    """Обработчик получения контакта инспектора"""
    contact: Contact = message.contact
    user_role, user = await add_role(
        contact=contact,
        role=IsInspector.role,
    )
    if not user:
        return

    if user_role:
        await message.answer("Этому сотруднику уже выдавалась роль инспектора")
    else:
        UserRole.get_or_create(user=user, role=IsInspector.role)
        await message.answer("Роль инспектора добавлена")
    await state.clear()

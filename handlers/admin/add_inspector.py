"""Обработчик добавления инспектора администратором"""
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.models import User, Role, UserRole
from states.admin.inspector import AddInspector
from filters.admin import IsAdmin

router = Router()


@router.message(F.text() == "Добавить инспектора", IsAdmin())
async def add_inspector_start(message: Message, state: FSMContext):
    """Обработчик начала добавления инспектора"""
    await message.answer("Отправьте контакт сотрудника")
    await state.set_state(AddInspector.get_contact)


@router.message(AddInspector.get_contact)
async def add_inspector_process(message: Message, state: FSMContext):
    """Обработчик получения контакта инспектора"""
    if message.contact:
        phone = message.contact.phone_number
        user_id = message.contact.user_id

        inspector, created = User.get_or_create(tg_id=user_id)

        if created:
            inspector.phone = phone
            inspector.username = message.contact.username
            inspector.first_name = message.contact.first_name
            inspector.last_name = message.contact.last_name
            inspector.save()
    else:
        try:
            user_id = int(message.text.strip())
            inspector, _ = User.get_or_create(tg_id=user_id)
        except ValueError:
            await message.answer(
                "Пожалуйста, отправьте контакт сотрудника или введите его ID"
            )
            return

    inspector_role = Role.get_or_none(name='Инспектор')
    if not inspector_role:
        await message.answer("В системе не найдена роль 'Инспектор'")
        await state.clear()
        return

    UserRole.get_or_create(user=inspector, role=inspector_role)
    await message.answer("Роль Инспектор добавлена")
    await state.clear()

"""Обработчик добавления инспектора администратором Addinspector"""
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.models import User, Role, UserRole
from states.admin.inspector import AddInspector

router = Router()


@router.message(F.text.lower() == "Добавить инспектора")
async def add_inspector_start(message: Message, state: FSMContext):
    """Обработчик начала добавления инспектора"""
    user = User.get_or_none(tg_id=message.from_user.id)
    if not user:
        return

    admin_role = Role.get_or_none(name='Администратор')
    is_admin = UserRole.get_or_none(user=user, role=admin_role)

    if not is_admin:
        await message.answer("У вас нет прав администратора")
        return

    await message.answer(
        "Введите ID пользователя Telegram, "
        "которого хотите назначить инспектором"
    )
    await state.set_state(AddInspector.get_contact)


@router.message(AddInspector.get_contact)
async def add_inspector_process(message: Message, state: FSMContext):
    """Обработчик получения ID инспектора"""
    try:
        inspector_id = int(message.text.strip())
    except ValueError:
        await message.answer(
            "Введите корректный ID пользователя (только цифры)"
        )
        return

    inspector, created = User.get_or_create(tg_id=inspector_id)
    if created:
        await message.answer(
            f"Пользователь с ID {inspector_id} добавлен в систему"
        )

    inspector_role = Role.get_or_none(name='Инспектор')
    if not inspector_role:
        await message.answer("В системе не найдена роль 'Инспектор'")
        await state.clear()
        return

    existing_role = UserRole.get_or_none(user=inspector, role=inspector_role)
    if existing_role:
        await message.answer(
            f"Пользователь с ID {inspector_id} уже является инспектором"
        )
    else:
        UserRole.create(user=inspector, role=inspector_role)
        await message.answer(
            f"Пользователь с ID {inspector_id} назначен инспектором"
        )

    await state.clear()

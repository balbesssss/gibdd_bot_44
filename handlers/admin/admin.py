"""Обработка команд Администратора"""
from aiogram import Router, F
from aiogram.types import Message, Contact
from filters.admin import IsAdmin
from aiogram.fsm.context import FSMContext
from states.admin.admin import AddAdmin
from database.models import User, Role, UserRole

router = Router()


@router.message(F.text == 'Добавить администратора', IsAdmin())
async def add_admin(message: Message, state: FSMContext):
    """Обработчик команды start"""

    await message.answer(
        text='Отправьте контакт сотрудника'
    )
    await state.set_state(AddAdmin.get_contact)


@router.message(F.contact, AddAdmin.get_contact, IsAdmin())
async def get_contact(message: Message, state: FSMContext):
    """Добавление администратора"""
    contact: Contact = message.contact
    role = Role.get(name='Администратор')
    if UserRole.get_or_none(
            user=User.get_or_none(tg_id=contact.user_id),
            role=role
            ) is None:
        UserRole.create(
            user=User.get(tg_id=contact.user_id),
            role=role
        )
        await message.answer("Роль Администратор добавлена")
    elif UserRole.get_or_none(
            user=User.get_or_none(tg_id=contact.user_id),
            role=role
            ):
        await message.answer(
            "Этому сотруднику уже выдавалась роль администратора"
            )
    else:
        await message.answer("Такой сотрудник не запускал бота")
        await message.answer(f"{contact.user_id}")
    await state.clear()

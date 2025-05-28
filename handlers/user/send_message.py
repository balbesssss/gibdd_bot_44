"""Пересылка сообщения от пользователя инспекторам"""

from typing import List
from aiogram import Router
from aiogram.types import Message
from filters.user import IsUser
from filters.inspector import IsInspector
from filters.admin import IsAdmin
from keyboards.inspector import user_ban_kb
from database.models import User, Admin, UserRole, Message as MessageModel

# pylint: disable=E1101

router = Router()


@router.message(IsUser())
async def get_message_from_user(message: Message):
    """Обработчик сообщения от пользователя"""
    await message.answer(
        "Спасибо за обращение. Мы его уже передали инспекторам"
    )
    user = User.get(User.tg_id == message.from_user.id)
    if user.is_ban:
        return

    admins = list(UserRole.select().where(UserRole.role == IsInspector.role))
    for admin in admins:
        message = await message.bot.send_message(
            chat_id=admin.user.tg_id,
            text=message.text,
            reply_markup=user_ban_kb(message.from_user.id),
        )

        MessageModel.get_or_create(
            to_inspector=admin.user.id,
            from_user=user.id,
            text=message.text,
            tg_message_id=message.message_id,
        )

    admins: List[User] = list(
        User.select()
        .join(UserRole, on=UserRole.user == User.id)
        .join(Admin, on=Admin.user == User.id)
        .where((Admin.is_notify) & (UserRole.role_id == IsAdmin.role.id))
    )
    for admin in admins:
        message = await message.bot.send_message(
            chat_id=admin.tg_id,
            text=message.text,
            reply_markup=user_ban_kb(message.from_user.id),
        )

        MessageModel.get_or_create(
            to_inspector=admin.id,
            from_user=user.id,
            text=message.text,
            tg_message_id=message.message_id,
        )

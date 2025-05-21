"""Пересылка сообщения от пользователя инспекторам"""

from aiogram import Router
from aiogram.types import Message
from database.models import UserRole
from filters.user import IsUser
from filters.inspector import IsInspector
from keyboards.user import MESUSER

router = Router()


@router.message(IsUser())
async def get_message_from_user(message: Message):
    """Обработчик сообщения от пользователя"""

    await message.answer(
        "Спасибо за обращение. Мы его уже передали инспекторам"
    )

    user_roles = list(
        UserRole.select().where(UserRole.role == IsInspector().role)
    )

    for user_role in user_roles:
        await message.bot.send_message(
            chat_id=user_role.user.tg_id, text=message.text, reply_markup=MESUSER
        )

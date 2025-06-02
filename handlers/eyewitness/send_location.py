"""Пересылка локации от пользователя инспекторам"""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.types import CallbackQuery
from filters.user import IsUser
from handlers.eyewitness.common import send_message_to_employees

from database.models import Location

# pylint: disable=E1101

router = Router()


@router.message(F.content_type == "location", IsUser())
async def get_location_from_user(message: Message):
    """Обработчик локации от пользователя"""

    await send_message_to_employees(message)

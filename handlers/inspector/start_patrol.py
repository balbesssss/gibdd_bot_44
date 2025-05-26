"""Начало патруля"""

from aiogram import Router, F
from aiogram.types import Message
from database.models import Patrol, User
from filters.inspector import IsInspector
from keyboards.common import get_kb_by_user


router = Router()


@router.message(F.text == 'Начать патрулирование', IsInspector())
async def start_patrol(message: Message):
    """Обработчик кнопки начала патруля"""
    inspector = User.get(tg_id=message.from_user.id)
    is_patrol = Patrol.get_or_none(
        (Patrol.inspector == inspector) &
        (Patrol.end.is_null())
        )
    if is_patrol:
        await message.answer("Вы уже в патруле",
                             reply_markup=get_kb_by_user(inspector),
                             )
    else:
        Patrol.create(inspector=inspector)
        await message.answer(
            "Патрулирование начато, "
            "теперь Вы будете получать сообщения от граждан",
        reply_markup=get_kb_by_user(inspector),
            )
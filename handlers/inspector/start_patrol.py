"""Начало патруля"""

from aiogram import Router, F
from aiogram.types import Message
from database.models import Patrol
from filters.inspector import IsInspector
from keyboards.common import get_kb_by_user
import handlers.inspector.common as c


router = Router()


@router.message(F.text == 'Начать патрулирование', IsInspector())
async def start_patrol(message: Message):
    """Обработчик кнопки начала патруля"""
    inspector, is_patrol = c.get_active_patrol(message.from_user.id)
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

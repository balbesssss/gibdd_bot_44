"""Завершение патруля"""

from datetime import datetime
from aiogram import Router, F
from aiogram.types import Message
from database.models import Patrol, User
from filters.inspector import IsInspector
from keyboards.common import get_kb_by_user


router = Router()


@router.message(F.text == 'Закончить патрулирование', IsInspector())
async def end_patrol(message: Message):
    """Обработчик кнопки завершения патруля"""
    inspector = User.get(tg_id=message.from_user.id)
    is_patrol = Patrol.get_or_none(
        (Patrol.inspector == inspector) &
        (Patrol.end.is_null())
        )
    if is_patrol:
        is_patrol.end = datetime.now()
        is_patrol.save()
        await message.answer(
            "Патрулировнаие закончено, "
            "теперь Вы не будете получать сообщения от граждан",
            reply_markup=get_kb_by_user(inspector)
        )
    else:
        await message.answer(
            "Вы уже не в патруле",
            reply_markup=get_kb_by_user(inspector)
        )

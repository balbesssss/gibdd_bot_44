"""Завершение патруля"""

from datetime import datetime
from aiogram import Router, F
from aiogram.types import Message
from filters.inspector import IsInspector
from keyboards.common import get_kb_by_user
from handlers.inspector.common import get_active_patrol


router = Router()


@router.message(F.text == "Закончить патрулирование", IsInspector())
async def end_patrol(message: Message):
    """Обработчик кнопки завершения патруля"""
    inspector, is_patrol = get_active_patrol(message.from_user.id)
    if is_patrol:
        is_patrol.end = datetime.now()
        is_patrol.save()
        await message.answer(
            "Патрулировнаие закончено, "
            "теперь Вы не будете получать сообщения от граждан",
            reply_markup=get_kb_by_user(inspector),
        )
    else:
        await message.answer(
            "Вы уже не в патруле", reply_markup=get_kb_by_user(inspector)
        )

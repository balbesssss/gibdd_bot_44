from aiogram.filters import BaseFilter
from aiogram.types import Message
from database.models import User


class IsUser(BaseFilter):
    """Проверяет, является ли пользователь."""
    async def __call__(self, message: Message) -> bool:
        return User.get_or_none(tg_id=message.from_user.id) is not None

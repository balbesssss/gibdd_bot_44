"""Библеотеки для проверки пользователя"""
from aiogram.filters import BaseFilter
from aiogram.types import Message
from database.models import Role, UserRole, User


class IsUser(BaseFilter):
    """Проверяет, является ли пользователь."""
    async def __call__(self, message: Message) -> bool:
        return User.get_or_none(tg_id=message.from_user.id) is not None


class IsAdmin(IsUser):
    """Проверяет является ли пользователь Администратором"""
    role = Role.get(name="Администратор")

    async def __call__(self, message: Message) -> bool:
        is_user = await super().__call__(message)
        if not is_user:
            return False

        user_role = UserRole.get_or_none(
            user=User.get(tg_id=message.from_user.id),
            role=self.role
        )
        return user_role is not None

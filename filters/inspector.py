"""Библеотеки для проверки Инспектора"""
from aiogram.types import Message
from database.models import Role, UserRole, User
from filters.user import IsUser


class IsInspector(IsUser):
    """Проверяет является ли пользователь Инспектором"""
    role = Role.get(name="Инспектор")

    async def __call__(self, message: Message) -> bool:
        is_user = await super().__call__(message)
        if not is_user:
            return False

        user_role = UserRole.get_or_none(
            user=User.get(tg_id=message.from_user.id),
            role=self.role
        )
        return user_role is not None

"""Библеотеки для проверки пользователя"""
from aiogram.filters import BaseFilter
from aiogram.types import Message
from database.models import Role, UserRole, User


class CheakAdmin(BaseFilter):
    """Проверяет является ли пользователь Администратором"""
    role = Role.get(Role.name == "Администратор")

    async def __call__(self, message: Message):
        if user := User.get_or_none(User.tg_id == message.from_user.id):
            if user_role := UserRole.get_or_none(UserRole.user == user):
                if user_role.role == self.role:
                    return True
        return False

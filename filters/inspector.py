"""Библеотеки для проверки Инспектора"""
from database.models import Role
from filters.user import IsUser


class IsInspector(IsUser):
    """Проверяет является ли пользователь Инспектором"""
    role = Role.get(name="Инспектор")

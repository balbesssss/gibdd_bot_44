"""Модель пользователя"""
# pylint: disable=R0903


class User:
    """Класс, представляющий пользователя."""
    def __init__(self, first_name=None, last_name=None):
        """Инициализация пользователя с именем и фамилией."""
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        """Возвращает полное имя пользователя."""
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

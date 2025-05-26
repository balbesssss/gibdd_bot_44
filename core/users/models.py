"""Модель пользователя"""


class User:
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name or ''} {self.last_name or ''}".strip()

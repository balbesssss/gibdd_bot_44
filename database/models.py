"""Модуль для базы данных"""

from datetime import datetime
from peewee import (
    SqliteDatabase,
    Model,
    CharField,
    IntegerField,
    DateTimeField,
    ForeignKeyField,
)

# pylint: disable=R0903
DB = SqliteDatabase("sqlite.db")


class Table(Model):
    """Базовая модель"""

    class Meta:
        """Класс мета"""

        database = DB


class User(Table):
    """Класс пользователя"""

    tg_id = IntegerField(unique=True)
    at_created = DateTimeField(default=datetime.now())
    username = CharField(null=True)
    last_name = CharField(null=True)
    first_name = CharField(null=True)
    phone = IntegerField(null=True)


class Role(Table):
    """Класс ролей"""

    name = CharField()


class UserRole(Table):
    """Класс роли пользователей"""

    user = ForeignKeyField(User, on_update="CASCADE", on_delete="CASCADE")
    role = ForeignKeyField(Role, on_update="CASCADE", on_delete="CASCADE")


class Message(Table):
    """Класс сообщений пользователя"""

    user = ForeignKeyField(User, on_update="CASCADE", on_delete="CASCADE")
    text = CharField(max_length=4096)
    at_created = DateTimeField(default=datetime.now())


class Patrol(Table):
    """Класс для сообщения о выезде инспектора"""

    inspector = ForeignKeyField(User, on_update="CASCADE", on_delete="CASCADE")
    at_created = DateTimeField(default=datetime.now())


if __name__ == "__main__":
    DB.connect()
    DB.create_tables([User, Role, UserRole, Message, Patrol], safe=True)
    DB.close()
    admin_role, _ = Role.get_or_create(name="Администратор")
    Role.get_or_create(name="Инспектор")
    admin, _ = User.get_or_create(tg_id=320720102)
    UserRole.get_or_create(
        user=admin,
        role=admin_role,
    )

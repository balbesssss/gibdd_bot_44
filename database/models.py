"""Модуль для базы данных"""
from peewee import SqliteDatabase, Model, CharField, IntegerField, DateField
from datetime import date
# pylint: disable=R0903
DB = SqliteDatabase('sqlite.db')


class Table(Model):
    """Базовая модель"""
    class Meta:
        """Класс мета"""
        database = DB


class User(Table):
    """Класс пользователя"""
    tg_id = IntegerField(unique=True)
    at_created = DateField(default=date.now())
    username = CharField(null=True)
    last_name = CharField(null=True)
    first_name = CharField(null=True)
    phone = IntegerField(null=True)


if __name__ == "__main__":
    DB.connect()
    DB.create_tables([User], safe=True)
    DB.close()

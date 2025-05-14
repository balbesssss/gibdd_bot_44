"""Модуль для базы данных"""
from peewee import SqliteDatabase, Model, CharField, IntegerField

DB = SqliteDatabase('sqlite.db')


class Table(Model):
    """Базовая модель"""
    class Meta:
        """Класс мета"""
        database = DB


class User(Table):
    """Класс пользователя"""
    tg_id = IntegerField(null=False, unique=True)
    username = CharField(null=True)
    last_name = CharField(null=True)
    first_name = CharField(null=True)
    telephone = IntegerField(null=True)


if __name__ == "__main__":
    DB.connect()
    DB.create_tables([User], safe=True)
    DB.close()

"""Модуль для базы данных"""
from peewee import SqliteDatabase, Model, CharField, IntegerField

DB = SqliteDatabase('sqlite.db')


class BaseModel(Model):
    """Базовая модель"""
    class Meta:
        """Класс мета"""
        database = DB


class User(BaseModel):
    """Класс пользователя"""
    tg_id = IntegerField(null=True)
    username = CharField(null=True)
    last_name = CharField(null=True)
    first_name = CharField(null=True)
    telephone = IntegerField(null=True)


if __name__ == "__main__":
    DB.connect()
    DB.create_tables([User], safe=True)
    DB.close()
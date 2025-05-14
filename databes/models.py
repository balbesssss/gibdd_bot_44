from peewee import SqliteDatabase, Model, CharField, IntegerField

DB = SqliteDatabase('sqlite.db')

class BaseModel(Model):
    class Meta:
        database = DB

class User(BaseModel):
    tg_id = IntegerField()
    username = CharField()
    last_name = CharField()
    first_name = CharField()
    telephone = IntegerField()

if __name__ == "__main__":
    DB.connect()
    DB.create_tables([User], safe = True)
    DB.close()
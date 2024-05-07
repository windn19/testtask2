from mixer.backend.peewee import Mixer
from peewee import CharField, TextField, ForeignKeyField, Model, SqliteDatabase

from . import db


class BaseModel(Model):
    class Meta:
        database = db


class UserType(BaseModel):
    name = CharField(max_length=20)


class User(BaseModel):
    name = CharField(max_length=20)
    email = CharField(max_length=30)
    image = CharField(max_length=50, null=True)
    typeID = ForeignKeyField(UserType, backref='users')

    def __repr__(self):
        return f'{self.name} - {self.password}'


class Order(BaseModel):
    title = CharField(max_length=20)
    describe = TextField()
    userID = ForeignKeyField(User, backref='orders')

    def __repr__(self):
        return f'{self.title}'


db.create_tables([User, UserType, Order])


if __name__ == '__main__':
    mixer = Mixer(locale='ru')
    # mixer.cycle(10).blend(User, typeID=mixer.SELECT, image=None)
    mixer.cycle(10).blend(Order, userID=mixer.RANDOM(2, 3, 4, 6, 7, 8))

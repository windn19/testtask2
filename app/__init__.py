from flask import Flask
from peewee import PostgresqlDatabase, SqliteDatabase


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_new_secret_key'

postgre = dict(database='site', user='postgres', password='postgres', host='localhost')

db = PostgresqlDatabase(**postgre)
# db = SqliteDatabase('base.db', check_same_thread=False)

from . import models, views, admins

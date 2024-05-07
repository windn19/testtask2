from flask import Flask
from peewee import PostgresqlDatabase


app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_new_secret_key'

postgre = dict(database='site', user='postgres', password='postgres', host='localhost')

db = PostgresqlDatabase(**postgre)

from . import models, views, admins

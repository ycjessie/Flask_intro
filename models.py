# https://git.generalassemb.ly/prudential-0921/flask-intro-get-post
# import * means import everything from peewee
from peewee import *
import datetime

# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('flask_dog_app', host='localhost', port=5432)

#schema
class Dog(Model):
    name = CharField()
    owner = CharField()
    breed = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Dog], safe=True)
    print("TABLES Created")
    DATABASE.close()
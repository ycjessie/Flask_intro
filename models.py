# https://git.generalassemb.ly/prudential-0921/flask-intro-get-post
# import * means import everything from peewee
from peewee import *
import datetime
#add user classes
#https://git.generalassemb.ly/prudential-0921/flask-register-login-dog-app#update-models
from flask_login import UserMixin


# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('flask_dog_app', 
host='localhost', port=5432)

#flask-login the interface for authentification purpose
class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    #hash the password not saving it
    password = CharField()
    
    # python: class object special construction instructions 
    # can be provided
    class Meta: #python class object,
        database = DATABASE
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
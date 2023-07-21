from mongoengine import *
from ....app import app

class Users(Document):
    username = StringField(required=True, unique=True)
    email = EmailField(required=True)
    age = IntField()

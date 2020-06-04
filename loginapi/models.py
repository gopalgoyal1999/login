from django.db import models
from mongoengine import *
# Create your models here.
connect(
    db = 'login-api',
    host='mongodb+srv://gopal:9582870584@cluster0-uvivi.mongodb.net/login-api?retryWrites=true&w=majority',
    username='gopal',
    password='9582870584'
)
class Login(Document):
    username = StringField(max_length=50 , required=True )
    email = StringField(max_length=50,required=True)
    password = StringField(required=True)

    def __str__(self):
        return self.username

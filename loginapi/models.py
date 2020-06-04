from django.db import models
from mongoengine import *
# Create your models here.
connect(
    db = 'login-api',
    host='mongodb+srv://gopal:**********@cluster0-uvivi.mongodb.net/login-api?retryWrites=true&w=majority',
    username='gopal',
    password='*********'
)
class Login(Document):
    username = StringField(max_length=50 , required=True )
    email = StringField(max_length=50,required=True)
    password = StringField(required=True)

    def __str__(self):
        return self.username

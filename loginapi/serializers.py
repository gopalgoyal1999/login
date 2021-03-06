from rest_framework_mongoengine import serializers
from .models import Login

class registerserializers(serializers.DocumentSerializer):
    class Meta:
        model = Login
        fields = ('username','email','password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 7},
                        #'email': {'write_only': True},
                        #'username': {'write_only': True}
                        }

class signserializers(serializers.DocumentSerializer):
    class Meta:
        model = Login
        fields = ('username','password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 7}}


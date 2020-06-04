from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from .models import Login
from .serializers import loginserializers

class RegistraionView(viewsets.ModelViewSet):

    lookup_field = 'id'
    serializer_class = loginserializers

    def get_queryset(self):
        return Login.objects.all()

    def post(self, request):
        serializer = loginserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),  # None
        }
        return Response(content)


'''
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework_mongoengine import viewsets


class LoginAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        # Get the username and password
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            raise exceptions.AuthenticationFailed(('No credentials provided.'))

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed(('Invalid username/password.'))

        if not user.is_active:
            raise exceptions.AuthenticationFailed(('User inactive or deleted.'))


        return (user, None)  # authentication successful


class LoginView(viewsets.ModelViewSet):
    authentication_classes = (SessionAuthentication, LoginAuthentication,)
    #permission_classes = (IsAuthenticated,)
    lookup_field = 'id'
    serializer_class = loginserializers

    def get_queryset(self):
        return Login.objects.all()

    def post(self, request):

        serializer = loginserializers(data=request.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistraionView(viewsets.ModelViewSet):

     lookup_field = 'id'
     serializer_class = loginserializers

     def get_queryset(self):
         return Login.objects.all()

     def post(self, request):
         serializer = loginserializers(data=request.data)
         if serializer.is_valid():
             serializer.save()
             return Response(status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
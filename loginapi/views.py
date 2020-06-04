from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from .models import Login
from .serializers import loginserializers,signserializers
from rest_framework.views import APIView

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


class LoginView(APIView):
    authentication_classes = (SessionAuthentication,BasicAuthentication)
    #permission_classes = (IsAuthenticated,)

    lookup_field = 'id'
    serializer_class = signserializers

    def post(self, request):
        groups = Login.objects.all()
        data = request.data
        serializer = signserializers(data=request.data)
        if serializer.is_valid():
            for group in groups:
                if data['password'] == group['password'] and data['username'] == group['username']:

                    return Response(status=status.HTTP_200_OK)
                else :
                    return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request, format=None):
    #     content = {
    #         'user': unicode(request.user),
    #         'auth': unicode(request.auth),  # None
    #     }
    #     return Response(content
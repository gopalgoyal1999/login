from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_mongoengine import viewsets
from rest_framework.response import Response
from .models import Login
from .serializers import registerserializers,signserializers
from rest_framework.views import APIView
from  django.shortcuts import redirect

class RegistraionView(viewsets.ModelViewSet):

    lookup_field = 'id'
    serializer_class = registerserializers

    def get_queryset(self):
        return Login.objects.all()

    def post(self, request):
        serializer = registerserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    lookup_field = 'id'
    serializer_class = signserializers

    def post(self, request):
        groups = Login.objects.all()
        username = request.POST.get('username')
        password = request.POST.get('password')
        serializer = signserializers(data=request.data)
        if serializer.is_valid():
            for group in groups:
                if password == group['password'] and username == group['username']:
                    request.session['m_id'] = password+username
                    return Response(status=status.HTTP_200_OK)

            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogOutView(APIView):
    # authentication_classes = (SessionAuthentication,)
    # permission_classes = (IsAuthenticated,)
    def post(self,request):
        if request.session['m_id'] != 0:
            print("SUCCESSFULLY LOGOUT")
            del request.session['m_id']
            return redirect('/login/')
        else :
            print("SIGN_IN / SIGN_UP ")
            return redirect('/login/')
        return Response(status=status.HTTP_200_OK)

#
# if data['password'] == group['password'] and data['username'] == group['username']:
#     request.session['m_id'] = data['password'] + data['username']
#     return Response(status=status.HTTP_200_OK)
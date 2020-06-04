from django.urls import path,include
from rest_framework_mongoengine import routers
from .views import LoginView,RegistraionView

router = routers.DefaultRouter()
router.register(r'login',LoginView,r"login")
router.register(r'register',RegistraionView, r"register")


urlpatterns = [
    path('',include(router.urls)),
]
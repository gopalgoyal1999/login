from django.urls import path,include
from rest_framework_mongoengine import routers
from .views import LoginView,RegistraionView,LogOutView

router = routers.DefaultRouter()
router.register(r'register',RegistraionView, r"register")

urlpatterns = [
    path('',include(router.urls)),
    path('login/',LoginView.as_view()),
    path('logout/',LogOutView.as_view())
]
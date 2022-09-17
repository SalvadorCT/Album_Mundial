from django.urls import path
from .views import RegistroUsuarioView
from rest_framework_simplejwt.views import TokenObtainPairView

#https://jwt.io/
urlpatterns = [
    path('registro', RegistroUsuarioView.as_view()),
    # tendremos un endpoint que servira para validar el usuario y si es,
    # correcto nos devolvera un token
    path('iniciar-sesion', TokenObtainPairView.as_view()),
]

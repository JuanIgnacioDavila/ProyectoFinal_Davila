
from django.urls import path
from AppCuenta.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('cuenta_login/',login_account,name='LoginCuenta'),
    path('cuenta_registro/',register_account,name='RegistroCuenta'),
    path('logout/',LogoutView.as_view(template_name="cuenta/logout.html"),name='accountLogout'),
    path('profile/',leer_perfil,name='LeerPerfil'),  
    path('edit_profile/',editar_perfil,name='EditarPerfil')     
]
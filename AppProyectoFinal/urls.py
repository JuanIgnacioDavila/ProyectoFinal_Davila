from django.urls import path
from AppProyectoFinal.views import *


urlpatterns = [
    path('about/',aboutme,name='About'),
    path('crearBlog/',crear_blog,name='CrearBlog'),
    path('leerBlog/',leer_blogs,name='LeerBlog'),
    path('eliminarBlog/<id>/',eliminar_blog,name='EliminarBlog'),
    path('editarBlog/<id>/',editar_blog,name='EditarBlog'),
    path('ver_mas/<id>/',ver_mas,name='VerMas'),   
    path('messages/<id>',mensajes,name='VerMensaje'),        
]
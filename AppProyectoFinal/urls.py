from django.urls import path
from AppProyectoFinal.views import *


urlpatterns = [
    path('about/',aboutme,name='About'),
    path('crearBlog/',crear_blog,name='CrearBlog'),
    path('leerBlog/',leer_blogs,name='LeerBlog'),
    path('eliminarBlog/<nombreb>/',eliminar_blog,name='EliminarBlog'),
    path('editarBlog/<nombre>/',editar_blog,name='EditarBlog'),
    path('ver_mas/<nombre>',ver_mas,name='ver_mas'),
    path('comentario/<nombre>/',agregar_comentario,name='AgregarComentario')
           
]
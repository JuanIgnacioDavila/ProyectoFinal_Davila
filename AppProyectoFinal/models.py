from django.db import models
from django.contrib.auth.models import User

class BlogsModel(models.Model):
    nombre=models.CharField(max_length=40)
    detalle=models.CharField(max_length=40)
    descripcion=models.TextField() 
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    fecha=models.DateField(auto_now_add=True)
    class Meta:
        db_table="Blogs" 
    def __str__(self):
        return f"Nombre: {self.nombre}'\n' Detalle: {self.detalle} Descripcion: {self.descripcion}"


class ComentariosModel(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(BlogsModel,on_delete=models.CASCADE)
    comentario=models.TextField()
    fecha=models.DateField(auto_now_add=True)
    class Meta:
        db_table="Comentarios"
    def __str__(self):
        return f"Nombre: {self.usuario}'\n Comentario: {self.comentario}"
from django.db import models

class BlogsModel(models.Model):
    nombre=models.CharField(unique=True,max_length=40)
    detalle=models.CharField(max_length=40)
    descripcion=models.TextField() 
    comentario=models.TextField()
    usuario=models.CharField(unique=True,max_length=40)
    class Meta:
        db_table="Blogs" 
    def __str__(self):
        return f"Nombre: {self.nombre}'\n' Detalle: {self.detalle} Descripcion: {self.descripcion}"


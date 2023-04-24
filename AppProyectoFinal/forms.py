from django import forms
from AppProyectoFinal.models import *

class BlogsForm(forms.ModelForm):
    class Meta:
        model=BlogsModel
        fields=("nombre","detalle","descripcion","imagen")

class BuscarBlogsForm(forms.Form):
    nombre=forms.CharField()

class ComentariosForm(forms.ModelForm):
    class Meta:
        model=ComentariosModel
        fields=("comentario",)

class BuscarComentariosForm(forms.Form):
    usuario=forms.CharField()
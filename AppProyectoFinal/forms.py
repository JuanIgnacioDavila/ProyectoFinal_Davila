from django import forms
from AppProyectoFinal.models import *

class BlogsForm(forms.ModelForm):
    class Meta:
        model=BlogsModel
        fields="__all__"

class BuscarBlogsForm(forms.Form):
    nombre=forms.CharField()
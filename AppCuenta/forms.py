#from AppCuenta.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
   
    imagen=forms.ImageField(required=False)
    descripcion=forms.CharField(widget=forms.Textarea)
    link=forms.CharField()
    class Meta():
        model=User
        fields=("username","first_name","imagen","email","link","descripcion")


class UserEditForm(forms.Form):
    #pk_url_kwarg='pk'
    imagen=forms.ImageField(required=False)
    email=forms.EmailField()
    link=forms.CharField()
    descripcion=forms.CharField(widget=forms.Textarea)




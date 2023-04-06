from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from AppCuenta.forms import *
from AppCuenta.models import *
from django.contrib.auth.decorators import login_required

def register_account(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            user=form.save()
            informacion=form.cleaned_data
            avatar=Avatar(
                user=user,
                imagen=informacion['imagen'],
                link=informacion['link'],
                descripcion=informacion['descripcion']
                )
            avatar.save()
            return redirect("LoginCuenta")
    form=UserRegistrationForm()
    context={
        "form":form,
    }
    return render(request,"cuenta/login.html",context)

def login_account(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        print(form.errors)
        if form.is_valid():
            informacion=form.cleaned_data
            user=authenticate(username=informacion['username'],password=informacion['password'])
            print(user)
            if user:
                login(request,user) ##logea el nuevo usuario y  elegimos donde queremos que se direccione
                return redirect("LoginCuenta")
            else:
                return redirect("RegistroCuenta")
    form=AuthenticationForm()
    context={
        "form":form,
        }
    return render(request,"cuenta/login.html",context=context)

def leer_perfil(request):
    """Me trae el perfil recien logueado,por lo tanto,filtro sin necesidad de colocar nombre,y solo ver los datos y tiene acceso al mismo el usuario que ha iniciado"""
    user = request.user
    profile = Avatar.objects.filter(user=user).first() 
    return render(request, 'cuenta/profile.html', {'profile': profile})


@login_required
def editar_perfil(request):
    user=request.user  ##Accedo al usuario
    if request.method=="POST":
        form=UserEditForm(request.POST,request.FILES)
        print(form.errors)
        if form.is_valid():
            
            informacion=form.cleaned_data
            user.avatar.descripcion=informacion['descripcion']            
            user.avatar.imagen=informacion['imagen']
            user.email=informacion['email']
            user.avatar.link=informacion['link']
          
            user.save()
            user.avatar.save()
           
            return redirect("LoginCuenta")
    form=UserEditForm(initial={
                
        "imagen":user.avatar.imagen,
        "email":user.email,
        "link":user.avatar.link,
        "descripcion":user.avatar.descripcion,
          })  ##Cargo el form del usuario
    
    context={
            "form":form,        
        }
    return render(request,"cuenta/edit_profile.html",context)

    

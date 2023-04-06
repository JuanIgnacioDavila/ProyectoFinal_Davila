from django.shortcuts import render,redirect
from AppProyectoFinal.models import *
from AppProyectoFinal.forms import *
from AppCuenta.models import *




def aboutme(request):
    return render(request,"AppProyectoFinal/aboutme.html")

def crear_blog(request):
    
    allproductos=BlogsModel.objects.all()
    context={
        "blogs":allproductos,
        "blogsform":BlogsForm(),
        "buscarblog":BuscarBlogsForm(),
    }

    if request.method =="POST":
        miForm=BlogsForm(request.POST)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            producto_save=BlogsModel(
                nombre=informacion['nombre'],
                detalle=informacion['detalle'],
                descripcion=informacion['descripcion'],
                comentario=informacion['comentario'],
                usuario=informacion['usuario']
                
            )
            producto_save.save()
            return redirect("CrearBlog")
    
           
    return render(request,"AppProyectoFinal/crearBlogs.html",context)    

def leer_blogs(request):
    filtro=BlogsModel.objects.all()
    context={
        "filtro":filtro,
        }
    return render(request,"AppProyectoFinal/blogs.html",context)

def eliminar_blog(request,nombreb):
    blog=BlogsModel.objects.get(nombre=nombreb)
    blog.delete()
    filtro=BlogsModel.objects.all()
    context={
        "filtro":filtro
    }
    return render(request,"AppProyectoFinal/blogs.html",context)

def editar_blog(request,nombre):
    user=user.username
    
    blog=BlogsModel.objects.get(nombre=nombre)
        
    if request.method =="POST":
        miForm=BlogsForm(request.POST)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            blog.nombre=informacion['nombre']
            blog.detalle=informacion['detalle']
            blog.descripcion=informacion['descripcion']
            blog.comentario=informacion['comentario']
            
                
            
            blog.save()
            return redirect("LeerBlog")
    context={
        "nombre":nombre,
        "form":BlogsForm(initial={
        "nombre":blog.nombre,
        "detalle":blog.detalle,
        "descripcion":blog.descripcion,
        "comentario":blog.comentario,
        })
    }
    return render(request,"AppProyectoFinal/editar.html",context)

def ver_mas(request,nombre):
    blog=BlogsModel.objects.get(nombre=nombre)
    context={
        "nombre":blog.nombre,
        "detalle":blog.detalle,
        "descripcion":blog.descripcion,
        "usuario":blog.usuario,
    }
    return render(request,"AppProyectoFinal/ver_mas.html",context)

def agregar_comentario(request,nombre):
    blog=BlogsModel.objects.get(nombre=nombre)
    if request.method=="POST":
        miForm=BlogsForm(request.POST)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            blog.comentario=informacion['comentario']  
            blog.save()
            return redirect("LeerBlog")
         

    context={
        "comentario":blog.comentario,
        "nombre":nombre,
        "form":BlogsForm(initial={
        "nombre":blog.nombre,
        "detalle":blog.detalle,
        "descripcion":blog.descripcion,
        "comentario":blog.comentario,})
        }
    return render(request,"AppProyectoFinal/comentario.html",context)


from django.shortcuts import render,redirect
from AppProyectoFinal.models import *
from AppProyectoFinal.forms import *

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
        miForm=BlogsForm(request.POST,request.FILES)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            producto_save=BlogsModel(
                nombre=informacion['nombre'],
                detalle=informacion['detalle'],
                descripcion=informacion['descripcion'],
                imagen=informacion['imagen'],
                
                usuario=request.user
                
            )
            producto_save.save()
            return redirect("LeerBlog")
    
           
    return render(request,"AppProyectoFinal/crearBlogs.html",context)    

def leer_blogs(request):
    filtro=BlogsModel.objects.all()
    us=request.user
    
    
    context={
        "us":us,
        "filtro":filtro,
        }
    return render(request,"AppProyectoFinal/blogs.html",context)

def eliminar_blog(request,id):
    blog=BlogsModel.objects.get(id=id)
    blog.delete()
    filtro=BlogsModel.objects.all()
    context={
        "filtro":filtro
    }
    return render(request,"AppProyectoFinal/blogs.html",context)

def editar_blog(request,id):
   
    blog=BlogsModel.objects.get(id=id)
        
    if request.method =="POST":
        miForm=BlogsForm(request.POST,request.FILES)
        print(miForm.errors)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            blog.nombre=informacion['nombre']
            blog.detalle=informacion['detalle']
            blog.descripcion=informacion['descripcion']
            blog.imagen=informacion['imagen']
        
            blog.save()
            return redirect("LeerBlog")
    context={
        "id":id,
        "form":BlogsForm(initial={
        "nombre":blog.nombre,
        "detalle":blog.detalle,
        "descripcion":blog.descripcion,
        "imagen":blog.imagen,
        })
    }
    return render(request,"AppProyectoFinal/editar.html",context)

def ver_mas(request,id):
    blog=BlogsModel.objects.get(id=id)
    
    if request.method =="POST":
        miForm=ComentariosForm(request.POST)
        print(miForm.errors)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            producto_save=ComentariosModel(
                usuario=request.user,
                blog=blog,
                comentario=informacion['comentario'],
                
            )
            producto_save.save()
            
    allcomentarios=ComentariosModel.objects.filter(blog=blog)  ##Condiciono de manera que solo muestre comentarios correspondientes a dicho blog           
    
    context={
        "id":id,
        "blog":blog,
        "comentarios":allcomentarios,
        "comentariosform":ComentariosForm(),
       
    }
    return render(request,"AppProyectoFinal/ver_mas.html",context)




def mensajes(request,id):
    blog=BlogsModel.objects.get(id=id)
    
    if request.method =="POST":
        miForm=ComentariosForm(request.POST)
        print(miForm.errors)
        if miForm.is_valid():
            informacion=miForm.cleaned_data
            producto_save=ComentariosModel(
                usuario=request.user,
                blog=blog,
                comentario=informacion['comentario'],
                
            )
            producto_save.save()
            
    allcomentarios=ComentariosModel.objects.filter(blog=blog)  ##Condiciono de manera que solo muestre comentarios correspondientes a dicho blog           
    
    context={
        "id":id,
        "blog":blog,
        "comentarios":allcomentarios,
        "comentariosform":ComentariosForm(),
       
    }
    return render(request,"AppProyectoFinal/mensajes.html",context)









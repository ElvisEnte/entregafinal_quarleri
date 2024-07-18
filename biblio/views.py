from django.shortcuts import render
from biblio.models import *
from biblio.forms import *
from django.views.generic import ListView



# Create your views here.
def home(request):
    return render(request, "biblio/index.html")



## _____Usuarios

def usuarios(request):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios": usuarios}
    return render(request, "biblio/usuarios.html", contexto)

def usuariosForm(request):
    
    if request.method == "POST":
        miForm = UsuarioForm(request.POST)
        if miForm.is_valid():
            nombre_usuario = miForm.cleaned_data.get("nombre")
            direccion_usuario = miForm.cleaned_data.get("direccion")
            email_usuario = miForm.cleaned_data.get("email")
            telefono_usuario = miForm.cleaned_data.get("telefono")
            usuario = Usuario(nombre=nombre_usuario, direccion=direccion_usuario, email=email_usuario, telefono=telefono_usuario)
            usuario.save()
            contexto = {"usuarios": Usuario.objects.all() }
            return render(request, "biblio/usuarios.html", contexto)
    else:
        miForm = UsuarioForm()
    
    return render(request, "biblio/usuarioForm.html", {"form": miForm})


## Libros

def libros(request):
    libros = Libro.objects.all()
    contexto = {"libros": libros}
    return render(request, "biblio/libros.html", contexto)


def librosForm(request):
    
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            titulo_libro = miForm.cleaned_data.get("titulo")
            autor_libro = miForm.cleaned_data.get("autor")
            anio_libro = miForm.cleaned_data.get("anio")
            genero_libro = miForm.cleaned_data.get("genero")
            libro = Libro(titulo=titulo_libro, autor=autor_libro, anio=anio_libro, genero=genero_libro)
            libro.save()
            contexto = {"libros": Libro.objects.all() }
            return render(request, "biblio/libros.html", contexto)
    else:
        miForm = LibroForm()
    
    return render(request, "biblio/librosForm.html", {"form": miForm})


def libroUpdate(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            libro.titulo = miForm.cleaned_data.get("titulo")
            libro.autor = miForm.cleaned_data.get("autor")
            libro.anio = miForm.cleaned_data.get("anio")
            libro.genero = miForm.cleaned_data.get("genero")
            libro.save()
            contexto = {"libros": Libro.objects.all() }
            return render(request, "biblio/libros.html", contexto)
    else:
        miForm = LibroForm(initial={"titulo": libro.titulo, "autor": libro.autor, "anio": libro.anio, "genero": libro.genero})

    return render(request, "biblio/librosForm.html", {"form": miForm})

def libroDelete(request, id_libro):
    libro = Libro.objects.get(id=id_libro)
    libro.delete()
    contexto = {"libros": Libro.objects.all() }
    return render(request, "biblio/libros.html", contexto)

## Proveedores

def direcciones(request):
    contexto = {"direcciones": Direccion.objects.all()}
    return render(request, "biblio/direcciones.html", contexto)

def direccionesForm(request):
    
    if request.method == "POST":
        miForm = DireccionesForm(request.POST)
        if miForm.is_valid():
            direcciones_calle = miForm.cleaned_data.get("calle")
            direcciones_altura = miForm.cleaned_data.get("altura")
            direcciones_timbre = miForm.cleaned_data.get("timbre")
            direcciones_barrio = miForm.cleaned_data.get("barrio")
            direcciones_nombre = miForm.cleaned_data.get("nombre")
            direcciones_telefono = miForm.cleaned_data.get("telefono")
            direcciones = Direccion(calle=direcciones_calle, altura=direcciones_altura, timbre=direcciones_timbre, barrio=direcciones_barrio,
                                  nombre=direcciones_nombre, telefono=direcciones_telefono)
            direcciones.save()
            contexto = {"direcciones": Direccion.objects.all() }
            return render(request, "biblio/direcciones.html", contexto)
    else:
        miForm = DireccionesForm()
    
    return render(request, "biblio/direccionForm.html", {"form": miForm})

## Buscar

def buscarLibros(request):
    return render(request, "negocio/buscarLibros.html")

def encontrarlibros(request):
    if request.GET["buscar"]:
        libro = request.GET["buscar"]
        titulos = Libro.objects.filter(titulo__icontains=libro)
        contexto = {'libros': titulos}
    else:
        contexto = {'libros': Libro.objects.all()}
        
    return render(request, "negocio/libros.html", contexto)
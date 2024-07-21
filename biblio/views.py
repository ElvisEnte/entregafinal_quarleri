import openpyxl
from django.conf import settings,os
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from biblio.models import *
from biblio.forms import *
from django.views.generic import ListView
from django.views.generic import CreateView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "biblio/index.html")

#____Catalogo
def catalogo(request):
    catalogo = 'datos/best_sellers.xlsx'
    datos = openpyxl.load_workbook(catalogo)
    hoja = datos.active
    

    for fila in hoja.iter_rows(min_row=2, values_only=True):
        titulo, autor, anio, genero = fila
        nombre_portada = f"{titulo}.png"
        ruta_portada = os.path.join('portadas', nombre_portada)
        default_cover_path = os.path.join('portadas', 'default.png')
        if not LibroCatalogo.objects.filter(titulo=titulo, autor=autor, anio=anio, genero=genero).exists():
            if os.path.exists(os.path.join(settings.MEDIA_ROOT, ruta_portada)):
                LibroCatalogo.objects.create(
                    titulo=titulo,
                    autor=autor,
                    anio=anio,
                    genero=genero,
                    portada=ruta_portada
                )
            else:
                portada = default_cover_path
                LibroCatalogo.objects.create(
                    titulo=titulo,
                    autor=autor,
                    anio=anio,
                    genero=genero,
                    portada = portada
                )
    libros = LibroCatalogo.objects.all()

    return render(request, "biblio/catalogo.html", {"catalogo": libros})

## Buscar
@login_required
def buscarLibros(request):
    return render(request, "biblio/buscarLibros.html")

def encontrarlibros(request):
    if request.GET["buscar"]:
        libro = request.GET["buscar"]
        titulos = LibroCatalogo.objects.filter(titulo__icontains=libro)
        contexto = {'libros': titulos}
    else:
        contexto = {'libros': LibroCatalogo.objects.all()}
        
    return render(request, "biblio/catalogo.html", contexto)

## _____Favoritos
@login_required
def favoritos(request):
    favoritos = Favorito.objects.all()
    contexto = {"favoritos": favoritos}
    return render(request, "biblio/favoritos.html", contexto)
@login_required
def favoritosForm(request):
    
    if request.method == "POST":
        miForm = FavoritosForm(request.POST)
        if miForm.is_valid():
            titulo_favorito = miForm.cleaned_data.get("titulo")
            autor_favorito = miForm.cleaned_data.get("autor")
            anio_favorito = miForm.cleaned_data.get("año")
            genero_favorito = miForm.cleaned_data.get("genero")
            nuevo_favorito = Favorito(titulo=titulo_favorito, autor=autor_favorito, anio=anio_favorito, genero=genero_favorito)
            nuevo_favorito.save()
            contexto = {"favoritos": Favorito.objects.all() }
            return render(request, "biblio/favoritos.html", contexto)
    else:
        miForm = FavoritosForm()
    
    return render(request, "biblio/favoritosForm.html", {"form": miForm})

def favoritosUpdate(request, id_favoritos):
    favoritos = Favorito.objects.get(id=id_favoritos)
    if request.method == "POST":
        miForm = FavoritosForm(request.POST)
        if miForm.is_valid():
            titulo_favorito = miForm.cleaned_data.get("titulo")
            autor_favorito = miForm.cleaned_data.get("autor")
            anio_favorito = miForm.cleaned_data.get("año")
            genero_favorito = miForm.cleaned_data.get("genero")
            favoritos = Favorito(titulo=titulo_favorito, autor=autor_favorito, anio=anio_favorito, genero=genero_favorito)
            favoritos.save()
            contexto = {"favoritos": Favorito.objects.all() }
            return render(request, "biblio/favoritosUpdate.html", contexto)
    else:
        miForm = FavoritosForm(initial={"titulo": titulo_favorito, "autor": autor_favorito, "anio": anio_favorito, "genero": genero_favorito})

@login_required
def favoritosDelete(request, id_favoritos):
    favoritos = Favorito.objects.get(id=id_favoritos)
    favoritos.delete()
    contexto = {"favoritos": Favorito.objects.all() }
    return render(request, "biblio/favoritos.html", contexto)

## Libros_usuario
@login_required
def libros(request):
    libros = LibroUsuario.objects.all()
    contexto = {"libros": libros}
    return render(request, "biblio/libros.html", contexto)

@login_required
def librosForm(request):
    
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            titulo_libro = miForm.cleaned_data.get("titulo")
            autor_libro = miForm.cleaned_data.get("autor")
            anio_libro = miForm.cleaned_data.get("anio")
            genero_libro = miForm.cleaned_data.get("genero")
            libro = LibroUsuario(titulo=titulo_libro, autor=autor_libro, anio=anio_libro, genero=genero_libro)
            libro.save()
            contexto = {"libros": LibroUsuario.objects.all() }
            return render(request, "biblio/libros.html", contexto)
    else:
        miForm = LibroForm()
    
    return render(request, "biblio/librosForm.html", {"form": miForm})

@login_required
def libroUpdate(request, id_libro):
    libro = LibroUsuario.objects.get(id=id_libro)
    if request.method == "POST":
        miForm = LibroForm(request.POST)
        if miForm.is_valid():
            libro.titulo = miForm.cleaned_data.get("titulo")
            libro.autor = miForm.cleaned_data.get("autor")
            libro.anio = miForm.cleaned_data.get("anio")
            libro.genero = miForm.cleaned_data.get("genero")
            libro.save()
            contexto = {"libros": LibroUsuario.objects.all() }
            return render(request, "biblio/libros.html", contexto)
    else:
        miForm = LibroForm(initial={"titulo": libro.titulo, "autor": libro.autor, "anio": libro.anio, "genero": libro.genero})

    return render(request, "biblio/librosForm.html", {"form": miForm})
@login_required
def libroDelete(request, id_libro):
    libro = LibroUsuario.objects.get(id=id_libro)
    libro.delete()
    contexto = {"libros": LibroUsuario.objects.all() }
    return render(request, "biblio/libros.html", contexto)

## Direcciones
@login_required
def direcciones(request):
    contexto = {"direcciones": Direccion.objects.all()}
    return render(request, "biblio/direcciones.html", contexto)
@login_required
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

@login_required
def direccionUpdate(request, id_direccion):
    direcciones = Direccion.objects.get(id=id_direccion)
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
        miForm = DireccionesForm(initial={"calle": direcciones_calle, "altura": direcciones_altura, "timbre": direcciones_timbre, "barrio": direcciones_barrio,
                                         "nombre": direcciones_nombre, "telefono": direcciones_telefono })

    return render(request, "biblio/direccionForm.html", {"form": miForm})
@login_required
def direccionDelete(request, id_direccion):
    direccion = Direccion.objects.get(id=id_direccion)
    direccion.delete()
    contexto = {"direcciones": Direccion.objects.all() }
    return render(request, "biblio/direcciones.html", contexto)



#___ Login / Logout / Registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            # Avatar
            try: 
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar

            return render(request, "biblio/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()
        
    return render(request, "biblio/login.html", {"form": miForm})
    
def crearUsuario(request):
    if request.method == "POST":
        miForm = CrearUsuarioForm(request.POST)
        if miForm.is_valid():
            try:
                miForm.save()
                return redirect(reverse('home'))
            except Exception as e:
                print(f"Error al guardar el formulario: {e}")
                return render(request, "biblio/crearUsuario.html", {"form": miForm})
        else:
            print(f"Errores en el formulario: {miForm.errors}")
            return render(request, "biblio/crearUsuario.html", {"form": miForm})
    else:
        miForm = CrearUsuarioForm()
        
        return render(request, "biblio/crearUsuario.html", {"form": miForm})
    
@login_required
def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        miForm = EditarForm(request.POST,instance=usuario)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse("home"))
    else:
        miForm = EditarForm(instance=usuario)
    return render(request, "biblio/editarUsuario.html", {"form": miForm})

class CambiarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = "biblio/cambiar_pass/html"
    success_url = reverse_lazy("home")



@login_required
def crearAvatar(request):
    usuario = request.user
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            
            avatarAnterior = Avatar.objects.filter(user=usuario)
            if len(avatarAnterior) > 0:
                for i in range(len(avatarAnterior)):
                    avatarAnterior[i].delete()
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()
            #Enviar la imagen a la home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen

            return redirect(reverse_lazy("home"))
    else:
        miForm = AvatarForm()
    return render(request, "biblio/agregar_avatar.html", {"form": miForm})

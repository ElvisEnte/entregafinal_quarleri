from django.urls import path
from biblio.views import *


urlpatterns = [
    path('', home, name="home"),
    
    ## Libros
    path('libros/', libros, name="libros"),
    path('librosForm/', librosForm, name="librosForm"),
    path('buscarLibros/', buscarLibros, name="buscarLibros"),
    path('encontrarlibros/', encontrarlibros, name="encontrarlibros"),
    path('libroUpdate/<id_libro>', libroUpdate, name="libroUpdate"),
    path('libroDelete/<id_libro>', libroDelete, name="libroDelete"),
    ## Usuarios
    path('usuarioForm/', usuariosForm, name="usuarioForm"),
    path('usuarios/', usuarios, name="usuarios"),
    
    ## Proveedores
    path('direcciones/', direcciones, name="direcciones"),
    path('direccionForm/', direccionesForm, name="direccionesForm"),
]

from django.urls import path
from biblio.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    
    ## Catalogo
    path('catalogo/', catalogo, name="catalogo"),
    
    ## Libros
    path('libros/', libros, name="libros"),
    path('librosForm/', librosForm, name="librosForm"),
    path('buscarLibros/', buscarLibros, name="buscarLibros"),
    path('encontrarlibros/', encontrarlibros, name="encontrarlibros"),
    path('libroUpdate/<id_libro>', libroUpdate, name="libroUpdate"),
    path('libroDelete/<id_libro>', libroDelete, name="libroDelete"),
    ## Favoritos
    path('favoritosForm/', favoritosForm, name="favoritosForm"),
    path('favoritos/', favoritos, name="favoritos"),
    path('favoritosUpdate/<int:id_favoritos>', favoritosUpdate, name="favoritosUpdate"),
    path('favoritosDelete/<id_favoritos>', favoritosDelete, name="favoritosDelete"),
    
    ## Direcciones
    path('direcciones/', direcciones, name="direcciones"),
    path('direccionForm/', direccionesForm, name="direccionesForm"),
    path('direccionUpdate/<int:id_direccion>', direccionUpdate, name="direccionUpdate"),
    path('direccionDelete/<int:id_direccion>', direccionDelete, name="direccionDelete"),
    
    #___ Login / Logout / Registration / Password / Avatar
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="biblio/logout.html"), name="logout"),
    path('crear/', crearUsuario, name="crear"),
    path('perfil/', editarUsuario, name="perfil"),
    path('<int:pk>/password/', CambiarPass.as_view(template_name="biblio/cambiar_pass.html"), name="password"),
    path('crearAvatar/', crearAvatar, name="crearAvatar"),
]

# Proyecto de Biblioteca en Línea

## Descripción

Este es un proyecto de biblioteca en línea desarrollado por Vicente Quarleri. El proyecto permite a los usuarios navegar por un catálogo de libros, buscar libros específicos y cargar nuevos libros.


## Características

- **Navegar por el Catálogo:** Los usuarios pueden ver una lista de libros disponibles con su portada, título, autor, año de publicación y género.
- **Buscar Libros:** Funcionalidad para buscar libros por título usando un formulario de búsqueda.
- **Cargar Libros:** Los usuarios autenticados pueden cargar sus libros que esten dispuestos a prestar por una comision
- **Domicilios:** Los usuarios pueden tambien indicar si tienen mas de un domicilio desde el cual retirar los libros que poseen o que quieren devolver
- **Imagen de Portada por Defecto:** Si un libro no tiene una imagen de portada, se muestra una imagen por defecto.

- ## Rutas URL

El proyecto utiliza las siguientes rutas URL para navegar entre las diferentes funcionalidades:

    ## Catalogo
    catalogo/',
    buscarLibros/',
    encontrarlibros/',
    
    ## Libros
    libros/',
    librosForm/',
    libroUpdate/<id_libro>',
    libroDelete/<id_libro>',
   
    ## Favoritos
    favoritosForm/',
    favoritos/',
    favoritosUpdate/<int:id_favoritos>',
    favoritosDelete/<id_favoritos>',
    
    ## Direcciones
    direcciones/',
    direccionForm/',
    direccionUpdate/<int:id_direccion>',
    direccionDelete/<int:id_direccion>',
    
    #___ Login / Logout / Registration / Password / Avatar
    login/', 
    logout/',
    crear/', 
    perfil/', 
    <int:pk>/password/',
    crearAvatar/',

### Users

user: admin
password: 12345


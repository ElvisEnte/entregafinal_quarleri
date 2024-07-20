from django.db import models


# Create your models here.

class Direccion(models.Model):
    calle = models.CharField(max_length=100)
    altura = models.IntegerField()
    timbre = models.CharField(max_length=50, default='Sin timbre')
    barrio = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50, default='Sin nombre')
    telefono = models.IntegerField()
    def __str__(self):
        return f"{self.nombre}, {self.calle} {self.altura}"
    
    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=250)
    email = models.EmailField()
    telefono = models.IntegerField()
    avatar = models.ImageField(upload_to='avatars/',null=True,blank=True)
    def __str__(self):
        return f"{self.nombre}"
    
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    anio = models.IntegerField()
    genero = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.titulo}"
    
    class Meta:
        ordering = ["titulo", "autor"]

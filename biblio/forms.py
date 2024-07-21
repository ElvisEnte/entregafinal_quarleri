from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class FavoritosForm(forms.Form):
    titulo = forms.CharField(max_length=50, required=True)
    autor = forms.CharField(max_length=200, required=True)
    año = forms.IntegerField(required=True)
    genero = forms.CharField(max_length=100, required=True)
    
class DireccionesForm(forms.Form):
    calle = forms.CharField(max_length=200, required=True)
    altura = forms.IntegerField(required=True)
    timbre = forms.CharField(max_length=50)
    barrio = forms.CharField(max_length=100, required=True)
    nombre = forms.CharField(max_length=50)
    telefono = forms.IntegerField(required=True)
    
    
class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=50, required=True)
    autor = forms.CharField(max_length=200, required=True)
    anio = forms.IntegerField(required=True, label="Año")
    genero = forms.CharField(max_length=100, required=True)
    
class CrearUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirma tu contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EditarForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="nombre", max_length=50)
    last_name = forms.CharField(label="apellido", max_length=50)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
    


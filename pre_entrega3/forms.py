from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class Alumno_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    comision = forms.IntegerField()

class Profesores_formulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    legajo = forms.IntegerField()


class Institucion_formulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    ciudad = forms.CharField(max_length=30)
    telefono = forms.IntegerField()

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar")
    password1 = forms.CharField(label="Contraseña" , widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña" , widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email','password1','password2']
        help_text = {k:"" for k in fields}
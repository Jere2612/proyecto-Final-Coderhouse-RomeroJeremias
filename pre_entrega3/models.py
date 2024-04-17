from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField(max_length=10)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} --- Comision: {self.comision}"
class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    legajo = models.IntegerField(max_length=10)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} --- Legajo: {self.legajo}"
class Institucion(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    telefono = models.IntegerField(max_length=20)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} --- Ciudad: {self.ciudad} --- Telefono: {self.telefono}"

class Avatar (models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)
    def __str__(self) -> str:
        return f"User: {self.user} --- Imagen: {self.imagen}"
from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()
    
    def __str__(self) -> str:
        return f"({self.comision}) {self.nombre}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    curso = models.CharField(max_length=30)
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.apellido}"
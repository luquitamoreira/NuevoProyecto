from django.db import models

# Create your models here.
class Estudiante(models.Model):
       nombre = models.CharField(max_length=100)
       edad = models.IntegerField()
       # Otros campos de tu modelo Estudiante

class Profesor(models.Model):
       nombre = models.CharField(max_length=100)
       especialidad = models.CharField(max_length=100)
       # Otros campos de tu modelo Profesor

class Curso(models.Model):
       nombre = models.CharField(max_length=100)
       descripcion = models.TextField()
       # Otros campos de tu modelo Curso
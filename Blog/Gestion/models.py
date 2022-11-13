from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=50)
    creditos = models.PositiveSmallIntegerField()


class Estudiante(models.Model):
    documento = models.CharField(primary_key=True, max_length=8)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

class Profesor(models.Model):
    ID = models.CharField(primary_key=True, max_length=4)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
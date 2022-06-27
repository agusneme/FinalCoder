from operator import truediv
from pyexpat import model
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class BlogModel2(models.Model):
    profesor = models.CharField(max_length=100)
    materia = models.CharField(max_length=100)
    tarea = models.TextField()
    autor2 = models.ForeignKey(User, on_delete=models.AutoField, null=True)
    fecha_creacion2 = models.DateField(auto_now_add=True)


class BlogModel(models.Model):
    titulo = models.CharField(max_length=100)
    sub_titulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.AutoField)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
        
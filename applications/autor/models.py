from django.db import models

#managers
from .managers import AutorManager

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id) + '-' + self.nombre + '-' + self.apellido


class Autor(Persona):
    seudonimo = models.CharField(
        'seudonimo', 
        max_length=50,
        blank=True
    )

    objects = AutorManager()

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    
from django.db import models

#managers
from .managers import AutorManager

# Create your models here.

class Autor(models.Model):
    """Model definition for Autor."""
    # TODO: Define fields here
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()

    objects = AutorManager()

    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        """Unicode representation of Autor."""
        return self.nombre + '-' + self.apellido

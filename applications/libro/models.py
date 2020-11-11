from django.db import models
from applications.autor.models import Autor
from .managers import LibroManager

# Create your models here.


class Categoria(models.Model):
    """Model de finition for Categoria."""
    nombre = models.CharField('Categoria', max_length=50)

    def __str__(self):
        """Unicode representation of Categoria."""
        return self.nombre


class Libro(models.Model):
    """Model definition for Libro."""
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    titulo = models.CharField(max_length=50)
    autores = models.ManyToManyField(Autor)
    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(upload_to='portada')
    visitas = models.PositiveIntegerField()
    
    objects = LibroManager()

    def __str__(self):
        """Unicode representation of Libro."""
        return self.titulo

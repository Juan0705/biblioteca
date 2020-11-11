from django.db import models
from applications.libro.models import Libro


# Create your models here.

class Lector(models.Model):
    """Model definition for Lector."""

    # TODO: Define fields here
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Lector'
        verbose_name_plural = 'Lectors'

    def __str__(self):
        """Unicode representation of Lector."""
        return self.nombre

class Prestamo(models.Model):
    """Model definition for Prestamo."""

    # TODO: Define fields here
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE
    )
    fecha_prestamo = models.DateField(auto_now=False, auto_now_add=False)
    fecha_devolucion = models.DateField(
        blank=True, 
        null=True, 
        auto_now=False, 
        auto_now_add=False
    )

    class Meta:
        """Meta definition for Prestamo."""

        verbose_name = 'Prestamo'
        verbose_name_plural = 'Prestamos'


    def __str__(self):
        """Unicode representation of Prestamo."""
        return self.libro.titulo


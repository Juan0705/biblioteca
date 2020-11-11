import datetime
from django.db import models
from django.db.models import Q

class LibroManager(models.Manager):
    '''manager para el modelo Autor'''

    def listar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2000-01-01','2020-01-01') #filtra por ese rango de fecha
        )
        return  resultado

    def listar_libros2(self, kword, fecha1, fecha2):

        # convertir formatos de fecha para ser aceptados
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2) #filtra por ese rango de fecha
        )
        return  resultado

    
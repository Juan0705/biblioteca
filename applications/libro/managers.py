import datetime
from django.db import models
from django.db.models import Q, Count
from django.contrib.postgres.search import TrigramSimilarity

class LibroManager(models.Manager):
    '''manager para el modelo Libro'''

    def listar_libros(self, kword):
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2000-01-01','2020-01-01') #filtra por ese rango de fecha
        )
        return  resultado

    def listar_libros_trg(self, kword):
        if kword:
            resultado = self.filter(
                titulo__trigram_similar=kword,
            )
            return  resultado
        else:
            return self.all()[:10]#retorna los primeros 10 elementos de toda la lista

    def listar_libros2(self, kword, fecha1, fecha2):

        # convertir formatos de fecha para ser aceptados
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2) #filtra por ese rango de fecha
        )
        return  resultado

    def listar_libros_categoria(self, categoria):

        return self.filter(
            categoria__id = categoria
        ).order_by('titulo')

    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)# se almacena el libro al que quiero agregarle un nuevo autor
        libro.autores.add(autor)
        return libro
    
    def remove_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)# se almacena el libro al que quiero eliminarle un autor
        libro.autores.remove(autor)
        return libro

    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado



class CategoriaManager(models.Manager):
    '''manager para el modelo Categoria'''

    #filtra las categorias por autor
    def categoria_por_autor(self, autor):
        return  self.filter(
            categoria_libro__autores__id=autor
        ).distinct()#"distinct" no repite valores dentro de la misma categoria 

    def listar_categoria_libros(self):
        resultado = self.annotate(
            num_libros = Count('categoria_libro')
        )
        return resultado

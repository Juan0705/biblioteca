from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    '''manager para el modelo Autor'''

    def listar_autores(self):
        return self.all()

    #filtra el nombre especifico del autor
    def buscar_autor(self, kword):
        resultado = self.filter(nombre=kword)
        return  resultado

    #filtra caracteres en el nombre del autor
    def buscar_autor_caracter(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        )
        return  resultado

    #filtrar con operador "or"
    def buscar_autor_or(self, kword):
        resultado = self.filter(
            #sentencia con operador "or"
            Q(nombre__icontains=kword) | Q(apellido__icontains=kword)
        )
        return  resultado

    #filtra con exclusiones
    def buscar_autor_excluir_edad(self, kword):
        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(
            Q(edad=34) | Q(edad=60)
        ) 
        return  resultado

    #filtra mayor, menor
    def buscar_autor_mayor_menor(self, kword):
        resultado = self.filter(
            edad__gt=40, #edad mayor a 40 (',' es and)
            edad__lt=65 # edad menor a 65
        ).order_by('apellido', 'nombre') # ordenar por apellido
        return  resultado
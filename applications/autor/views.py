from django.shortcuts import render

from django.views.generic import ListView
#models local
from applications.autor.models import Autor

# Create your views here.


class ListAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = "autor/lista.html"

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword', '')
        
        return Autor.objects.buscar_autor_mayor_menor(palabra_clave)

    
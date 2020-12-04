from datetime import date

from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.views.generic.edit import FormView

from .models import Prestamo
from .forms import PrestamoForm, MultiplePrestamoForm


class RegistrarPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.' # al recargar direcciona a la misma vista

    def form_valid(self, form):

        '''
        # siempre crea una nueva instancia
        Prestamo.objects.create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )
        '''
        # crea una nueva instancio o guarda los cambios de una instancia y creada
        prestamo = Prestamo(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )
        prestamo.save()

        libro = form.cleaned_data['libro']
        libro.stok = libro.stok - 1
        libro.save()

        return super(RegistrarPrestamo, self).form_valid(form)

class AddPrestamo(FormView):
    template_name = 'lector/add_prestamo.html'
    form_class = PrestamoForm
    success_url = '.'

    def form_valid(self, form):

        # si existe lo recupera, si no existe lo crea
        obj, created = Prestamo.objects.get_or_create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto=False,
            defaults={
                'fecha_prestamo':date.today()
            }
        )

        if created: # si el registro es creado se recarga la pagina
            return super(AddPrestamo, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')# si ya existe el registro se redirecciona a otra url


class AddMultiplePrestamo(FormView):
    template_name = 'lector/add_multiple_prestamo.html'
    form_class = MultiplePrestamoForm
    success_url = '.' 

    def form_valid(self, form):
        prestamos = []
        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
            lector=form.cleaned_data['lector'],
            libro=l,
            fecha_prestamo=date.today(),
            devuelto=False
            )
            prestamos.append(prestamo)

        Prestamo.objects.bulk_create( # 'bulk_create' registra todo en una sola consulta
            prestamos
        )

        return super(AddMultiplePrestamo, self).form_valid(form)
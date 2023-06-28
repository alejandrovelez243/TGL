from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Libro

# Create your views here.

def vista_libroHttpResponse(request):
    return HttpResponse("Aqui se mostraran los libros")

def vista_libro(request):
    libros = Libro.objects.all()
    return render(request, 'libros.html', {'libros': libros})


class TemplateVistaLibro(TemplateView):
    template_name = "libros_template.html"

    def get_context_data(self, **kwargs):
        context = super(TemplateVistaLibro, self).get_context_data(**kwargs)
        context["libros"] = ["Libro 1", "Libro 2", "Libro 3", "Libro 4"]
        return context

class ListListaLibro(ListView):
    model = Libro
    template_name = "libros_lista.html"
    context_object_name = "libros_list"

    def get_queryset(self):
        queryset = self.model.objects.filter(publicado__year=2023)
        return queryset



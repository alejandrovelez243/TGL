from django.urls import path
from .views import vista_libro, TemplateVistaLibro, ListListaLibro

urlpatterns = [
    path('libros', vista_libro, name='vista_libro'),
    path('libros_template', TemplateVistaLibro.as_view(), name='libros_template'),
    path('libros_lista', ListListaLibro.as_view(), name='libros_lista')
]

from customer.views import *
from django.urls import path


urlpatterns = [
    path("crear", crear_objeto),
    path("obtener", obtener_objeto),
    path("actualizar", actualizar_objecto),
    path("eliminar", eliminar_objecto),
    path("consultas_relacionadas", consultas_relacionadas),
    path("consultas_complejas", consultas_complejas),
]

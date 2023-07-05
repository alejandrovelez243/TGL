from customer.views import *
from django.urls import path


urlpatterns = [
    path("crear", crear_objeto),
    path("obtener", obtener_objeto),
    path("actualizar", actualizar_objecto),
    path("eliminar", eliminar_objecto),
    path("consultas_relacionadas", consultas_relacionadas),
    path("consultas_complejas", consultas_complejas),
    path("agregaciones", agregaciones),
    path("subconsultas", subconsultas),
    path("transacciones", transacciones),
    path("prueba_cache", prueba_cache),
    path("celery_suma", celery_suma),
    path("tarea_no_celery", tarea_no_celery),
    path("tarea_celery", tarea_celery),
]

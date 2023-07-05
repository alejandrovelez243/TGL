from django.shortcuts import render
from django.http import HttpResponse
from film.models import Category
from customer.models import Customer
from rental.models import Rental
from film.models import Film
from django.db.models import Q, Count, Subquery, Sum
from django.db import transaction
from django.core.cache import cache
from .tasks import add, tarea_larga

# Create your views here.

# Ejemplos basicos

def crear_objeto(request):
    category = Category(name="Prueba 3")
    category.save()
    category = Category.objects.create(name="Prueba 4")
    return HttpResponse(category.name)


def obtener_objeto(request):
    category = Category.objects.get(name="Prueba")
    return HttpResponse(category.name)


def actualizar_objecto(request):
    # category = Category.objects.get(name="Prueba")
    # category.name = "Ficción"
    # category.save()
    category = Category.objects.filter(name="Prueba 3")
    category.update(name="Cambiado con update")
    return HttpResponse([cat.name for cat in category])


def eliminar_objecto(request):
    categories = Category.objects.filter(name="Prueba 4")
    for category in categories:
        print(category.name)
        category.delete()
    Category.objects.filter(name="Cambiado con update").delete()
    return HttpResponse("Elimine las pruebas")

# Hasta acá son ejemplos basicos de CRUD (Create, read, update, delete)


# Ejemplos complejos

def consultas_relacionadas(request):
    rentals = Rental.objects.filter(customer_id__username="admin")
    for rental in rentals:
        print(rental.inventor_id.film_id.title)
    return HttpResponse(f"Usuarios encontados {[str(rental.return_date) for rental in rentals]}")


def consultas_complejas(request):
    films = Film.objects.filter(Q(title__startswith="R") | Q(category__name__icontains="f") | Q(category__name__contains="f"))
    # icontains no es case sensitive y contains es case senstivie, osea le importan las mayusculas y minisculas
    return HttpResponse("Encotradas")



def agregaciones(request):
    # cuentas_usuarios = Customer.objects.filter(id=1).aggregate(usuarios=Count('id'), sumas=Sum("id"))
    cuentas_usuarios = Customer.objects.aggregate(usuarios=Count('id'), sumas=Sum("id"))
    print(cuentas_usuarios["usuarios"])

    return HttpResponse(f"Tienes estos usuarios {cuentas_usuarios}")


def subconsultas(request):
    ultimo_login = Customer.objects.filter(last_login__date=Subquery(Customer.objects.order_by('-last_login').values("last_login__date")[:1]))

    print(ultimo_login)
    return HttpResponse(f"Tienes estos usuarios {ultimo_login}")


def transacciones(request):
    try:
        Category.objects.create(name="No fallo")
        with transaction.atomic():
            Category.objects.create(name="Fallo")
            algo = 1 / 0

        return HttpResponse("Categoria creada")
    except Exception as e:
        return HttpResponse("Categoria fallo")



# aqui acaba clase de ORM



# Aqui empieza clase de redis y celery

def prueba_cache(request):

    cache.set("my_key", "Hello World", 600)

    value = cache.get("my_key")

    return HttpResponse("La cache fue creada y consultada")

# ejemplo no funcional en vistas, en este caso porque paises no lo tenemos en los modelos.

def decordaror_cache(funcion_original):
    def funcion_envolvente(*args, **kwargs):
        paises = cache.get("paises")
        if not paises:
            paises = funcion_original(*args, **kwargs)
        cache.set("paises", paises, 600)
        return paises
    return funcion_envolvente


@decordaror_cache
def regresar_paises(request):
    paises = Paises.objects.all()
    return paises


def celery_suma(request):
    # La tarea se ejecutará en segundo plano y la vista retornará inmediatamente.
    result = add.delay(4, 4)
    print(result.get(timeout=10))
    return HttpResponse('Task has been run')


def tarea_no_celery(request):
    tarea_larga()
    return HttpResponse('Tarea se ejecuto sin celery')

def tarea_celery(request):
    tarea_larga.delay()
    return HttpResponse('Tarea se ejecuto con celery')
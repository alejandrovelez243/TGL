from django.shortcuts import render
from django.http import HttpResponse
from film.models import Category
from rental.models import Rental
from film.models import Film
from django.db.models import Q

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

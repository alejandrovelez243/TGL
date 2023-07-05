from celery import shared_task
import time

@shared_task
def add(x, y):
    print("YA estoy funcionando al fin")
    return x + y

@shared_task
def tarea_larga():
    for i in range(10):
        print(f"Espera {i}")
        time.sleep(1)
    print("Termine")
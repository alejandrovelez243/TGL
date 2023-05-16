
def range_unico():
    for i in range(4):
        print(i)

def range_multiple():
    for i in range(2, 10):
        print(i)

def range_steps():
    for i in range(2, 10, 2):
        print(i)

def iterar_lista():
    lista = ["Valor 1", "Valor 2", "Valor 3"]
    for valor in lista:
        print(valor)

    for indice, valor in enumerate(lista):
        print(f"{indice} {valor}")

def iterar_lista_range():
    lista = ["Valor 1", "Valor 2", "Valor 3"]
    for indice in range(len(lista)):
        print(lista[indice])

def iterar_diccionario():
    diccinario = {"Nombre": "Alejandro", "Apellido": "Velez", "Edad": 25}

    for clave in diccinario:
        print(diccinario[clave])

    for clave in diccinario.keys():
        print(clave)

    for valor in diccinario.values():
        print(valor)

    for clave, valor in diccinario.items():
        print(f"{clave} {valor}")



def while_generico():
    numero = 1
    while numero < 5:
        print(numero)
        numero += 1

def do_while():
    numero = 1
    while True:
        if numero == 5:
            break
        print(numero)
        numero += 1
    print("Finalice")


def continue_list():

    lista = ["Valor 1", "valor 2", "Valor 3"]

    for valor in lista:
        if valor == "valor 2":
            continue
        print(valor)

continue_list()



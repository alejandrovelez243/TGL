

def operacion_and(a, b):
    print(a and b)

operacion_and(True, True)
operacion_and(False, True)
operacion_and(False, False)

def operacion_or(a, b):
    print("Operacion or", a or b)

operacion_or(True, False)
operacion_or(False, False)
operacion_or(10, 1)


def operacion_not(a):
    print(not a)

operacion_not(True)

a = input("Ingresa el primer valor")
print(type(a))



def operaciones(a, b):
    a = int(a)
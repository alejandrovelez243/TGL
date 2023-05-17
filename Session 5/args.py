
def primeros_args(*args):
    print(args[0])

    operacion = args[0] + sum(args[2])
    print(operacion)

    for value in args:
        print(value)



primeros_args(2, "Hola", [1,2,3], "Adios")


lista_args = ["Lista", "Argumentos", "Prueba"]

primeros_args(*lista_args)



def funcion_parametro():
    print("Soy la funcion parametro")



def primeros_kwargs(primer_parametro, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} {value}")
        if callable(value):
            value()
    print(primer_parametro)



diccionario = {"hola": "Persona", "Edad": 23, "funcion": funcion_parametro}

primeros_kwargs(primer_parametro="Primero", **diccionario)
primeros_kwargs("Primero", hola="Persona", Edad=23,funcion=funcion_parametro)


# Asignacion simple
a = 2
SOY_GLOBAL = "SOY GLOBAL"
print(a)

# Asignacion multiple
b, c, d = 2, 3.233, "String"

print(b)
print(c)
print(d)


# asignar resultados de funciones
def retornar():
    return "Retorne un valor"


def variables_global():
    global SOY_GLOBAL
    local = "Soy local"
    SOY_GLOBAL = "CAMBIO DE VALOR"

retornado = retornar()

print(retornado)
print(SOY_GLOBAL)
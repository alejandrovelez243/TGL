lista_1 = [1, 2, "Texto", ["Otra lista", 2, 4]]
print(lista_1)
print(type(lista_1)) # obtenemos el tipo de dato

lista_append = [5, 2, 34]

lista_append.append("Final")

print(lista_append)

lista_remove = [5, 6, 7, 76]

lista_remove.remove(6)

print(lista_remove)

lista_sort = [753, 6, 5, 23, 321, ]

lista_sort.sort()

print(lista_sort)

lista_sort.sort(reverse=True)

print(lista_sort)


lista_sort = ["B", "Manuela", "Pepito", "A"]

lista_sort.sort(reverse=True)

print(lista_sort)


lista_reverse = ["B", "Manuela", "Pepito", "A"]

lista_reverse.reverse()

print(lista_reverse)

lista = ["B", "Manuela", "Pepito", "A", "Ultimo"]

print(lista.index("B"))

print(lista.count("B"))


print(len(lista))

print(sum([5, 6, 3]))


print(lista[0:3])

print(lista[-1])
print(lista[len(lista) - 1])

lista.pop(2)
print(lista)

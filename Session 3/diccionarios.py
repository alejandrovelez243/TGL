diccionario = {
    "nombre": "Alejandro",
    "edad": "25",
    "trabajo": "desarrollador",
    "mascotas": ["Gea", "Floki"],
    "mascotas_completo": [
        {
            "nombre": "Gea",
            "edad": 1
        }
    ]
}

print(diccionario)


print(diccionario.keys())


print(diccionario.values())

print(diccionario.items())

print(diccionario["nombre"])

print(diccionario.get("apellido", "No tiene apellido"))

diccionario["mascotas"].append("Mascota3")

print(diccionario)

print(diccionario["mascotas_completo"][0]["nombre"])

diccionario["nombre"] = "Alejandro Velez"

print(diccionario)

diccionario.update({"nombre": "Alejandro Patiño"})
diccionario.update({"apellido": "Velez"})

print(diccionario)

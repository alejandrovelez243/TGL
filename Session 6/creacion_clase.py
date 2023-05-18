
# animales_bosque!?*  # Las variables y clases no pueden contener caracteres especiales, ni iniciar con un numero


class Perro:
    nombre = "" # Es una buena practica tener los atributos organizados
    color = ""
    edad = 0

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def despedir(self):
        print(f"Me despido desde la funcion 'despedir' {self.nombre}")

    def saludar(self):
        print(f"Hola me llamo {self.nombre}, y tengo {self.edad} años")
        self.despedir() # llamado a una función interna de la clase

    def asignar_color(self, color):
        self.color = color

    def __str__(self):
        return "Soy un objeto perro"

perro = Perro("Juanes", 5)

print(perro)

perro.saludar()

perro.despedir()



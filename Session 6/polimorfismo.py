

class Ave:
    def volar(self):
        pass


class Aguila(Ave):

    def volar(self):
        print("Puedo volar")


class Pinguino(Ave):

    def volar(self):
        print("No puedo volar")

aguila = Aguila()

aguila.volar()

pinguino = Pinguino()

pinguino.volar()




class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        pass


class Perro(Animal):
    def sonido(self):
        return "guau"


class Gato(Animal):
    def sonido(self):
        return "miau"


class Pajaro(Animal):
    def sonido(self):
        return "pio"


perro = Perro("MAx", 3)

print(f"{perro.nombre} hace el sonido {perro.sonido()}")

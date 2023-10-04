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
animales = []

while True:
    print("Seleccione una opción:")
    print("1. Agregar Perro")
    print("2. Agregar Gato")
    print("3. Agregar Pájaro")
    print("4. Mostrar Animales")
    print("5. Salir")

    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del perro: ")
        edad = input("Ingrese la edad del perro: ")
        perro = Perro(nombre, edad)
        animales.append(perro)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del gato: ")
        edad = input("Ingrese la edad del gato: ")
        gato = Gato(nombre, edad)
        animales.append(gato)

    elif opcion == "3":
        nombre = input("Ingrese el nombre del pájaro: ")
        edad = input("Ingrese la edad del pájaro: ")
        pajaro = Pajaro(nombre, edad)
        animales.append(pajaro)

    elif opcion == "4":
        print("\nListado de Animales:")
        for animal in animales:
            print(f"Nombre: {animal.nombre}, Edad: {animal.edad}, Sonido: {animal.sonido()}")
            print("--------------------")

    elif opcion == "5":
        break

    else:
        print("Opción no válida. Por favor, elija una opción válida.")
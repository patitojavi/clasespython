


class Pasajero:
    def __init__(self, nombre, apellido, num_pasaporte):
        self.nombre = nombre
        self.apellido = apellido
        self.num_pasaporte = num_pasaporte

    def __str__(self):
        return f"{self.nombre} {self.apellido}, Pasaporte: {self.num_pasaporte}"


class Vuelo:
    def __init__(self, num_vuelo, destino):
        self.num_vuelo = num_vuelo
        self.destino = destino
        self.pasajeros = []

    def embarcar_pasajero(self, pasajero):
        self.pasajeros.append(pasajero)
        print(f"Se ha embarcado al pasajero: {pasajero.nombre} {pasajero.apellido}")

    def desembarcar_pasajero(self, num_pasaporte):
        for pasajero in self.pasajeros:
            if pasajero.num_pasaporte == num_pasaporte:
                self.pasajeros.remove(pasajero)
                print(f"Se ha desembarcado al pasajero: {pasajero.nombre} {pasajero.apellido}")
                return
        print(f"No se encontró al pasajero con el pasaporte: {num_pasaporte}")

    def mostrar_lista_pasajeros(self):
        print("\nLista de pasajeros del vuelo:")
        for pasajero in self.pasajeros:
            print(pasajero)


vuelo1 = Vuelo("ABC123", "Nueva York")
vuelo2 = Vuelo("XYZ789", "París")

menu = """  
Menú:
1. Embarcar pasajero
2. Desembarcar pasajero
3. Mostrar lista de pasajeros
4. Cambiar de vuelo
5. Salir 
"""


while True:
    print(menu)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del pasajero: ")
        apellido = input("Ingrese el apellido del pasajero: ")
        num_pasaporte = input("Ingrese el número de pasaporte del pasajero: ")
        pasajero = Pasajero(nombre, apellido, num_pasaporte)
        vuelo1.embarcar_pasajero(pasajero)

    elif opcion == "2":
        num_pasaporte = input("Ingrese el número de pasaporte del pasajero a desembarcar: ")
        vuelo1.desembarcar_pasajero(num_pasaporte)

    elif opcion == "3":
        vuelo1.mostrar_lista_pasajeros()

    elif opcion == "4":
        nuevo_destino = input("Ingrese el nuevo destino del vuelo: ")
        vuelo1 = Vuelo(vuelo1.num_vuelo, nuevo_destino)

    elif opcion == "5":
        break

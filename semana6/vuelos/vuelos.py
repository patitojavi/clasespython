class Reserva:
    def __init__(self, pasajero, vuelo, fecha):
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.fecha = fecha
        

    def mostrar_detalle(self):
        pass  


class ReservaEconomica(Reserva):
    def __init__(self, pasajero, vuelo, fecha, asiento):
        super().__init__(pasajero, vuelo, fecha)
        self.asiento = asiento

    def mostrar_detalle(self):
        return f"Reserva Económica - Pasajero: {self.pasajero}, Vuelo: {self.vuelo}, Fecha: {self.fecha}, Asiento: {self.asiento}"


class ReservaBusiness(Reserva):
    def __init__(self, pasajero, vuelo, fecha, asiento_negocio):
        super().__init__(pasajero, vuelo, fecha)
        self.asiento_negocio = asiento_negocio

    def mostrar_detalle(self):
        return f"Reserva Business - Pasajero: {self.pasajero}, Vuelo: {self.vuelo}, Fecha: {self.fecha}, Asiento Negocio: {self.asiento_negocio}"


class ReservaPrimeraClase(Reserva):
    def __init__(self, pasajero, vuelo, fecha, asientovip):
        super().__init__(pasajero, vuelo, fecha)
        self.asientovip = asientovip

    def mostrar_detalle(self):
        return f"Reserva Primera Clase - Pasajero: {self.pasajero}, Vuelo: {self.vuelo}, Fecha: {self.fecha}, Asiento Vip: {self.asientovip}"


reservas = []

while True:

    pasajero = input("Nombre del pasajero: ")
    vuelo = input("Número de vuelo: ")
    fecha = input("Fecha de vuelo: ")


    tipo_reserva = input("Tipo de reserva (Economica/Business/PrimeraClase): ").lower()

    if tipo_reserva == "economica":
        asiento = input("Número de asiento: ")
        reserva = ReservaEconomica(pasajero, vuelo, fecha, asiento)
    elif tipo_reserva == "negocio":
        asiento_negocio = input("Número de asiento de negocios: ")
        reserva = ReservaBusiness(pasajero, vuelo, fecha, asiento_negocio)
    elif tipo_reserva == "primerclase":
        asientovip = input("Número de asiento VIP: ")
        reserva = ReservaPrimeraClase(pasajero, vuelo, fecha, asientovip)
    else:
        print("Tipo de reserva no válido. Inténtalo de nuevo.")
        continue
    reservas.append(reserva)

    otra_reserva = input("¿Deseas hacer otra reserva? (si/no): ")
    if otra_reserva.lower() != "si":
        break

for reserva in reservas:
    print(reserva.mostrar_detalle())
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

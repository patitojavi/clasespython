


class Jugador:
    def __init__(self, nombre, puntaje=0):
        if not nombre.strip():
            raise ValueError("El nombre del jugador no puede estar vacío o contener solo espacios en blanco.")
        if puntaje < 0:
            raise ValueError("El puntaje no puede ser negativo.")
        
        self.nombre = nombre
        self.puntaje = puntaje

    def aumentar_puntaje(self, cantidad, bonificacion=0):
        if cantidad < 0 or bonificacion < 0:
            raise ValueError("La cantidad y la bonificación deben ser valores positivos.")
        
        self.puntaje += cantidad + bonificacion

    def mostrar_puntaje(self):
        return self.puntaje
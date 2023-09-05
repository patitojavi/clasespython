class Rectangulo:
    def __init__(self, longitud, ancho):  
        self.longitud = longitud
        self.ancho = ancho

    def calcularArea(self):
        return self.longitud * self.ancho

    def calcularPerimetro(self):
        return 2 * (self.longitud + self.ancho)

longitud = float(input("Dame la longitud del rectángulo: "))
ancho = float(input("Dame el ancho del rectángulo: "))
rectangulo = Rectangulo(longitud, ancho)
print("El área del rectángulo es:", rectangulo.calcularArea())
print("El perímetro del rectángulo es:", rectangulo.calcularPerimetro())
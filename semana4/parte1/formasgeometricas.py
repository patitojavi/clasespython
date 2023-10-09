import math

class FormaGeometrica:
    def __init__(self, alto, ancho):
        if alto < 0 or ancho < 0:
            raise ValueError("Las dimensiones no pueden ser negativas")
        self.alto = alto
        self.ancho = ancho

    def area(self):
        pass

    def perimetro(self):
        pass


class Rectangulo(FormaGeometrica):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)

    def area(self):
        return self.alto * self.ancho

    def perimetro(self):
        return 2 * (self.alto + self.ancho)


class Triangulo(FormaGeometrica):
    def __init__(self, base, altura):
        super().__init__(altura, base)

    def area(self):
        return 0.5 * self.alto * self.ancho

    def perimetro(self):
        raise ValueError("El perímetro de un triángulo no se puede calcular sin información adicional")


class Circulo(FormaGeometrica):
    def __init__(self, radio):
        super().__init__(0, 0)  
        if radio < 0:
            raise ValueError("El radio no puede ser negativo")
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2

    def perimetro(self):
        return 2 * math.pi * self.radio



try:
    rectangulo = Rectangulo(5, 10)
    print(f"Área del rectángulo: {rectangulo.area()}")
    print(f"Perímetro del rectángulo: {rectangulo.perimetro()}")

    triangulo = Triangulo(4, 6)
    print(f"Área del triángulo: {triangulo.area()}")
    triangulo.perimetro()

    circulo = Circulo(3)
    print(f"Área del círculo: {circulo.area()}")
    print(f"Perímetro del círculo: {circulo.perimetro()}")

except ValueError as e:
    print(f"Error: {e}")

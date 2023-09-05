class Circulo:
    def __init__(self, radio):  # Cambié "init" a "__init__" para que sea el constructor.
        self.radio = radio

    def calcularArea(self):
        numeropi = 3.14
        return numeropi * self.radio ** 2  
    def calcularPerimetro(self):
        numeropi = 3.14
        return 2 * numeropi * self.radio

    def cambiarRadio(self, nuevoradio):
        self.radio = nuevoradio 

radio = float(input("Dame el radio del círculo: "))
circulo = Circulo(radio)
print("El área del círculo es:", circulo.calcularArea())
print("El perímetro del círculo es:", circulo.calcularPerimetro())
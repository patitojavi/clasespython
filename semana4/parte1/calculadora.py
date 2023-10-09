


class Calculadora:
    def __init__(self):
        pass
    
    def suma(self, a, b, c = None):
        if c is None:
            return a + b
        else:
            return a + b + c
    
    def resta(self, a, b):
            return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return "no se puede dividir por 0"

    def cuadrado(self, a):
        return a ** 2

    def cubo(self,a):
        return a ** 3


menu = """ 
ingrese 1 para sumar 
ingrese 2 para restar
ingrese 3 para multiplicar
ingrese 4 para dividir
ingrese 5 para sacar el cuadrado
ingrese 6 para el cubo
ingrese q para salir"""

calculadora = Calculadora()

while True:
    print(menu)
    opcion = input("ingrese una opcion: ")
    
    if opcion == "1":
        a = float(input("ingrese el numero a sumar: "))
        b = float(input("ingrese el numero a sumar: "))
        total = calculadora.suma(a,b)
        print(f"el resultado es: {total}")
    elif opcion == "2":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        total = calculadora.resta(a, b)
        print("Resultado de la resta:", total)
    elif opcion == "3":
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        total = calculadora.multiplicacion(a, b)
        print("Resultado de la multiplicación:", total)
    elif opcion == "4":
        a = float(input("Ingrese el numerador: "))
        b = float(input("Ingrese el denominador: "))
        if b == 0:
            print("Error: No se puede dividir entre cero.")
            
        else:
            total = calculadora.division(a, b)
            print("Resultado de la división:", total)
    elif opcion == "5":
        a = float(input("Ingrese el número para calcular su cuadrado: "))
        total = calculadora.cuadrado(a)
        print("Resultado del cuadrado:", total)
    elif opcion == "6":
        a = float(input("Ingrese el número para calcular su cubo: "))
        total = calculadora.cubo(a)
        print("Resultado del cubo:", total)
    elif opcion.lower() == "q":
        break
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
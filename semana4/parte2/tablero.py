import random

class Tablero:
    def __init__(self, N):
        if N <= 0:
            raise ValueError("El tamaño del tablero debe ser un número positivo mayor que cero.")
        
        self.N = N
        self.tablero = [[0 for _ in range(N)] for _ in range(N)]
        self.tesoro_x, self.tesoro_y = random.randint(0, N - 1), random.randint(0, N - 1)
        self.trampa_x, self.trampa_y = random.randint(0, N - 1), random.randint(0, N - 1)
        while self.trampa_x == self.tesoro_x and self.trampa_y == self.tesoro_y:
            self.trampa_x, self.trampa_y = random.randint(0, N - 1), random.randint(0, N - 1)

        self.tablero[self.tesoro_x][self.tesoro_y] = 'T'
        self.tablero[self.trampa_x][self.trampa_y] = 'X'

    def mostrar_matriz(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.tablero[i][j] == 'T' or self.tablero[i][j] == 'X':
                    print('0', end=' ')
                else:
                    print(self.tablero[i][j], end=' ')
            print()
    
    def adivinar_posicion(self, x, y):
        if x < 0 or x >= self.N or y < 0 or y >= self.N:
            print("Coordenadas inválidas. Debe ingresar coordenadas dentro del rango del tablero.")
            return

        if self.tablero[x][y] == 'T':
            print("Has encontrado el tesoro. ¡ganaste!")
            return True
        elif self.tablero[x][y] == 'X':
            print("caíste en la trampa. ¡Perdiste!")
            return True
        else:
            print("No has encontrado nada en estas coordenadas.")
            return False

# Ejemplo de uso
try:
    N = int(input("Ingrese el tamaño del tablero (N x N): "))
    tablero = Tablero(N)
except ValueError as e:
    print(e)
else:
    while True:
        tablero.mostrar_matriz()
        coordenadas = input("Adivina las coordenadas (por ejemplo, '3 4' o [3,4]): ")
        
        try:
            if len(coordenadas.split()) == 2:
                x, y = map(int, coordenadas.split())
            elif len(coordenadas.strip("[").strip("]").split(",")) == 2:
                x, y = map(int, coordenadas.strip("[").strip("]").split(","))
            else:
                print("formato de coordenadas no válido.")
                continue
        except ValueError:
            print("coordenadas inválidas. debe ingresar dos números separados por un espacio o una lista con dos números.")
            continue
        
        if tablero.adivinar_posicion(x, y):
            break

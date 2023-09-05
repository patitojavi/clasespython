import random

class Playlist: # se crea una clase llamada playlist                                                                 
    def __init__(self, nombre): 
        self.nombre = nombre # se asigna el valor argumento nombre
        self.canciones = [] # se inicializa el atributo como una lista vacia, para almacenar canciones
        self.estado = "detenido" # se inicializa el atributo con el valor detenido, se usa para controlar si se esta reproduciendo o no
        self.indice_reproduccion = 0

    def agregar_cancion(self, cancion): # se define el metodo agregar cancion, que pertenece a playlist
        self.canciones.append(cancion) # agrega las canciones a la lista vacia canciones

    def eliminar_cancion(self, indice): # esto define el metodo eliminar cancion, para eliminarla de la lista
        if 0 <= indice < len(self.canciones): # esta linea verifica si el indice esta dentro de los limites validos en la lista de canciones y 
                                            # devuelve la cantidad de elementos en la lista de canciones, por lo que esta condición se asegura de que el índice esté dentro del rango válido.
            del self.canciones[indice]      # si se cumple la condicion, elimina la cancion correspondiente

    def mostrar_canciones(self): # se define el metodo mostrar canciones para mostrar todas las canciones en la lista        
        for i, cancion in enumerate(self.canciones): # este for recorre a traves de todas las canciones en la lista de reproduccion y se usa enumerate para obtener el indice y valor de cada cancion
            print("=" * 50) # i = indice - cancion = el valor de la cancion
            print(f"{i}: - {cancion}")

    def reproducir(self): # se define el metodo reproducir para reproducir las canciones
        if self.estado == "detenido" or self.estado == "pausa": # si el estado es detenido o pausa, se cambia a reproduciendo
            self.estado = "reproduciendo" # esta funcion solo hace el cambio de estado
            print("=" * 50)
            print(f"reproduciendo: {self.canciones[self.indice_reproduccion]}")

    def seleccionar_cancion(self, indice): # se define el metodo seleccionar cancion para seleccionar la cancion por su indice de la lista de reproduccion
        if 0 <= indice < len(self.canciones): # verifica si el indice esta dentro de la lista de canciones
            self.indice_reproduccion = indice # si se cumple la condicion, se actualiza el atributo indice_reproduccion
            self.estado = "detenido" # tambien se cambia el estado a detenido
            self.reproducir() # 

    def pausar(self): # se define el metodo pausar para pausar la cancion
        if self.estado == "reproduciendo": # si el estado es reproduciendo, se cambia a pausa
            self.estado = "pausa"
            print("=" * 50)
            print("pausado")


    def detener(self): # se define el metodo detener para detener la reproduccion
        if self.estado == "reproduciendo" or self.estado == "pausa": # si el estado es reproduciendo o en pausa, se cambia a detenido
            self.estado = "detenido"
            print("=" * 50)
            print("detenido")


    def siguiente(self): # se define el metodo siguiente para reproducir la siguiente cancion
        if self.estado == "reproduciendo": # si el estado es reproduciendo....
            self.indice_reproduccion = (self.indice_reproduccion + 1) % len(self.canciones) # calcula el indice de la proxima cancion incrementando en 1 la cancion actual
            self.reproducir() # se inicia la reproduccion 

    def anterior(self): # se define el metodo anterior para reproducir la cancion anterior
        if self.estado == "reproduciendo": # verifica si está en reproduciendo el estado,
            self.indice_reproduccion = (self.indice_reproduccion - 1) % len(self.canciones) # si es asi se calcula la cancion anterior decrementando en 1 la canciona ctual
            self.reproducir()  # se inicia el metodo reproduccion

    def reproducir_aleatorio(self): # se define el metodo aleatorio para reproducir una cancion aleatoria de la lista
        if self.estado == "reproduciendo": # verifica si el estaod es reproduciendo, si es así entonces mostrara por pantalla que ya esta reproduciendose
            print("=" * 50)
            print("ya estás reproduciendo una canción.")
        else:
            indice_aleatorio = random.randint(0, len(self.canciones) - 1) # sino, se usa el random para iniciar una cancion aleatoria por su indice
            self.seleccionar_cancion(indice_aleatorio) # se inicia el metodo seleccionar cancion con el indice aleatorio

    def estado_actual(self): # se define el metodo estado actual para mostrar por pantalla el nombre de la playlist, estado y cancion actual
        print("=" * 50)
        print(f"nombre de la Playlist: {self.nombre}")
        print(f"estado: {self.estado}")
        print(f"canción actual: {self.canciones[self.indice_reproduccion] if self.canciones else 'Ninguna'}")

def menu_principal():
    print(""" 
===================================================
                    Spotify                         
===================================================

selecciona una opcion: 


         1)     ♪     agregar canción    ♪
         2)     ♪    eliminar canción    ♪
         3)     ♪    mostrar canciones   ♪
         4)     ♪   seleccionar canción  ♪
         5)     ►       reproducir       ►
         6)     ║║        pausar        ║║
         7)     ▄         detener        ▄
         8)     ►►       siguiente      ►►
         9)     ◄◄       anterior       ◄◄ 
        10)     ↕  reproducir aleatorio  ↕
        11)     ♪      estado actual     ♪
        12)     ♪         salir          ♪


===================================================
""")

nombre_playlist = input("crea una playlist: ")
playlist = Playlist(nombre_playlist)

while True:
    menu_principal()

    opcion = input("ingresa una opción:  ")

    if opcion == "1":
        cancion = input("nombre de la cancion:  ")
        playlist.agregar_cancion(cancion)
    elif opcion == "2":
        indice = int(input("numero de la cancion para eliminar: "))
        playlist.eliminar_cancion(indice)
    elif opcion == "3":
        
        print("canciones en la playlist: ")
        playlist.mostrar_canciones()
    elif opcion == "4":
        indice = int(input("ingrese el índice de la canción a seleccionar: "))
        playlist.seleccionar_cancion(indice)
    elif opcion == "5":
        playlist.reproducir()
    elif opcion == "6":
        playlist.pausar()
    elif opcion == "7":
        playlist.detener()
    elif opcion == "8":
        playlist.siguiente()
    elif opcion == "9":
        playlist.anterior()
    elif opcion == "10":
        playlist.reproducir_aleatorio()
    elif opcion == "11":
        playlist.estado_actual()
    elif opcion == "12":
        print("saliendo de spotify.")
        break
    else:
        print("opción no válida, intente de nuevo.")



class Tarea:
    def __init__(self, nombre, descripcion, completada=False):
        self.nombre = nombre
        self.descripcion = descripcion
        self.completada = completada

    def completar(self):
        self.completada = True

    def descripcion(self):
        return self.descripcion



tareas = []
menu = """"
agregar tarea 1
marcar tarea 2
ver tarea 3
salir 4
"""

while True:
    print(menu)
    
    opcion = input("ingrese una opcion")
    
    if opcion == "1":
        tar = str(input("ingrese la tarea a realizar:"))
        des = str(input("ingrese una descripcion:"))
        tarea = Tarea(tar, des)
        tareas.append(tarea)
        print("tarea registrada con exito")
    elif opcion == "2":
        tarea_index = int(input("Ingrese el índice de la tarea a marcar como completada: "))
        if tarea_index >= 0 and tarea_index < len(tareas):
            tareas[tarea_index].completar()
            print(f"Tarea '{tareas[tarea_index].nombre}' marcada como completada.")
        else:
            print("Índice de tarea fuera de rango.")
    elif opcion == "3":
        tarea_index = int(input("Ingrese el índice de la tarea para mostrar su descripción: "))
        if tarea_index >= 0 and tarea_index < len(tareas):
            descripcion = tareas[tarea_index].obtener_descripcion()
            print(f"Descripción de la tarea '{tareas[tarea_index].nombre}': {descripcion}")
        else:
            print("Índice de tarea fuera de rango.")
    
    elif opcion == "4":
        break
    
    else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
        
class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.calificaciones = []

    def agregar_calificacion(self, calificacion):
        if isinstance(calificacion, (int, float)) and 0 <= calificacion <= 10:
            self.calificaciones.append(calificacion)
            print(f"Calificación {calificacion} agregada para el estudiante {self.nombre}")
        elif isinstance(calificacion, list):
            for calif in calificacion:
                if isinstance(calif, (int, float)) and 0 <= calif <= 10:
                    self.calificaciones.append(calif)
                    print(f"Calificación {calif} agregada para el estudiante {self.nombre}")
                else:
                    print(f"Calificación no válida: {calif}")
        else:
            print(f"Calificación no válida: {calificacion}")

    def promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

    def estado(self):
        promedio = self.promedio()
        if promedio >= 6:
            return "Aprobado"
        else:
            return "Reprobado"
class Estudiante:
    def __init__(self, nombre, matricula):
        self.__nombre = nombre
        self.__matricula = matricula
    
    def get_nombre(self):
        return self.__nombre
    
    def get_matricula(self):
        return self.__matricula
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    def set_matricula(self, nueva_matricula):
        self.__matricula= nueva_matricula



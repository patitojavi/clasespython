

class Carro:
    def __init__(self, marca, modelo, año):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def get_año(self):
        return self.__año
    
    def set_marca(self, nueva_marca):
        self.__marca= nueva_marca
    
    def set_modelo(self, nuevo_modelo):
        self.__modelo = nuevo_modelo
        
    def set_año(self, nuevo_año):
        self.__año = nuevo_año
        



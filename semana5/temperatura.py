class Termometro:
    def __init__(self):
        self.__temperatura  = 15
    
    def get_temperatura(self):
        return self.__temperatura
    
    def set_temperatura(self, nueva_temperatura):
        if 10<= nueva_temperatura <=30:
            self.__temperatura = nueva_temperatura
        else:
            print("la temperatura no puede ser menor a 10 y mayor a 30 grados")
    
    
    def aumentar_temperatura(self):
        if self.__temperatura < 30:
            self.__temperatura += 1
        else:
            print("la temperatura no puede superar los 30 grados")
    
    
    def disminuir_temperatura(self):
        if self.__temperatura < 30:
            self.__temperatura -= 1
        else:
            print("no puede ser inferior a 10 grados")
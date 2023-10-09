class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def entrar_al_edificio(self,edificio):
        edificio.registrar_entrada(self)
    
    def salir_del_edificio(self,edificio):
        edificio.registrar_salida(self)


class Edificio:
    personas_en_edificio = []


    @staticmethod
    
    def registrar_entrada(persona):
        Edificio.personas_en_edificio.append(persona)
        print(f"{persona.nombre} ha entrado al edificio")
        
    @staticmethod
    
    def registrar_salida(persona):
        if persona in Edificio.personas_en_edificio:
            Edificio.personas_en_edificio.remove(persona)
            print(f"{persona.nombre} ha salido del edificio")
        else:
            print(f"{persona.nombre} no estaba en el edificio")
    
    def mostrar_personas_en_edificio():
        print("personas en el edificio: ")
        for persona in Edificio.personas_en_edificio:
            print(f"- {persona.nombre}")



class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def unirse_al_chat(self, chat):
        chat.agregar_usuario(self)

    def salir_del_chat(self, chat):
        chat.eliminar_usuario(self)


class Chat:
    usuarios_en_linea = set()

    @staticmethod
    def agregar_usuario(usuario):
        Chat.usuarios_en_linea.add(usuario)
        print(f'{usuario.nombre} se ha unido al chat.')

    @staticmethod
    def eliminar_usuario(usuario):
        if usuario in Chat.usuarios_en_linea:
            Chat.usuarios_en_linea.remove(usuario)
            print(f'{usuario.nombre} ha salido del chat.')
        else:
            print(f'{usuario.nombre} no estaba en línea.')

    @staticmethod
    def mostrar_usuarios_en_linea():
        print('Usuarios en línea:')
        for usuario in Chat.usuarios_en_linea:
            print(f'- {usuario.nombre}')


# Ejemplo de uso
if __name__ == "__main__":
    usuario1 = Usuario("Usuario1")
    usuario2 = Usuario("Usuario2")
    usuario3 = Usuario("Usuario3")

    chat = Chat()

    usuario1.unirse_al_chat(chat)
    usuario2.unirse_al_chat(chat)
    usuario3.unirse_al_chat(chat)

    Chat.mostrar_usuarios_en_linea()

    usuario2.salir_del_chat(chat)

    Chat.mostrar_usuarios_en_linea()

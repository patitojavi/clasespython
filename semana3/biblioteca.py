# Pasos
# 1) Definir la clase Libro
class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def __str__(self):
        return f"'{self.titulo}' por {self.autor}, {self.num_paginas} páginas"
# Definir la clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        if not isinstance(libro, Libro):
            print("El objeto no es un libro válido.")
            return
        self.libros.append(libro)

    def buscar_por_titulo(self, titulo):
        resultado = [str(libro) for libro in self.libros if libro.titulo == titulo]
        return resultado

    def buscar_por_autor(self, autor):
        resultado = [str(libro) for libro in self.libros if libro.autor == autor]
        return resultado

    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)
# Uso
# Crear algunos libros
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1023)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 417)
libro3 = Libro("La sombra del viento", "Carlos Ruiz Zafón", 544)

# Crear una biblioteca y agregar los libros
biblioteca = Biblioteca()
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Mostrar los libros
biblioteca.mostrar_libros()

# Buscar libros por autor y título
print("\nLibros de Miguel de Cervantes:")
print(biblioteca.buscar_por_autor("Miguel de Cervantes"))

print("\nLibros titulados 'Cien años de soledad':")
print(biblioteca.buscar_por_titulo("Cien años de soledad"))


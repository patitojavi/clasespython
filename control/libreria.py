class Libro:
    def __init__(self, id, autor, titulo):
        self.id = id
        self.autor = autor
        self.titulo = titulo

    def __str__(self):
        return f"ID: {self.id}, Autor: {self.autor}, Título: {self.titulo}"


libros = {}

def agregar_libro(id, autor, titulo):
    if id in libros:
        print(f"Ya existe un libro con ID {id}. No se ha agregado el libro.")
    else:
        nuevo_libro = Libro(id, autor, titulo)
        libros[id] = nuevo_libro
        print(f"Libro agregado con éxito (ID {id}):")
        print(nuevo_libro)

def buscar_libro_por_id(id):
    if id in libros:
        libro_encontrado = libros[id]
        print(f"Libro encontrado (ID {id}):")
        print(libro_encontrado)
    else:
        print(f"No se encontró un libro con ID {id}")


agregar_libro(1, "George Orwell", "1984")
agregar_libro(2, "Harper Lee", "Matar a un ruiseñor")
agregar_libro(3, "Miguel de Cervantes", "Don Quijote de la Mancha")
agregar_libro(4, "Gabriel García Márquez", "Cien años de soledad")
agregar_libro(5, "J.K. Rowling", "Harry Potter y la Piedra Filosofal")
agregar_libro(6, "F. Scott Fitzgerald", "El Gran Gatsby")
agregar_libro(7, "Fyodor Dostoevsky", "Crimen y Castigo")
agregar_libro(8, "J.R.R. Tolkien", "El Señor de los Anillos: La Comunidad del Anillo")
agregar_libro(9, "Suzanne Collins", "Los juegos del hambre")
agregar_libro(10, "Jane Austen", "Orgullo y prejuicio")
agregar_libro(11, "Herman Melville", "Moby-Dick")
agregar_libro(12, "James Joyce", "Ulises")
agregar_libro(13, "Marcel Proust", "En busca del tiempo perdido")
agregar_libro(14, "J.R.R. Tolkien", "El Hobbit")
agregar_libro(15, "Emily Brontë", "Cumbres Borrascosas")
agregar_libro(16, "Homero", "La Odisea")
agregar_libro(17, "Franz Kafka", "La Metamorfosis")
agregar_libro(18, "Victor Hugo", "Los Miserables")
agregar_libro(19, "Antoine de Saint-Exupéry", "El principito")
agregar_libro(20, "Gabriel García Márquez", "Cien años de soledad")


while True:
    print("Opciones:")
    print("1. Agregar libro")
    print("2. Buscar libro por ID")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        id = int(input("Ingrese el ID del libro: "))
        autor = input("Ingrese el autor del libro: ")
        titulo = input("Ingrese el título del libro: ")
        agregar_libro(id, autor, titulo)
        
    elif opcion == "2":
        id_a_buscar = int(input("Ingrese el ID del libro a buscar: "))
        buscar_libro_por_id(id_a_buscar)
        
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

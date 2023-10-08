

class Estudiante:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.cursos_inscritos = []

    def inscribir_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.agregar_estudiante(self)
            print(f"{self.nombre, self.apellido} se ha inscrito en el curso: {curso}")

    def desinscribir_curso(self, curso):
        if curso in self.cursos_inscritos:
            self.cursos_inscritos.remove(curso)
            curso.eliminar_estudiante(self)
            print(f"{self.nombre} {self.apellido} se ha desinscrito del curso: {curso}")

    def __str__(self):
        return f"{self.nombres} {self.apellido}"


class Curso:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estudiantes_inscritos = []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.estudiantes_inscritos:
            self.estudiantes_inscritos.append(estudiante)

    def eliminar_estudiante(self, estudiante):
        if estudiante in self.estudiantes_inscritos:
            self.estudiantes_inscritos.remove(estudiante)

    def __str__(self):
        return f"{self.nombre} - {self.descripcion}"



estudiantes = []
cursos = []
menu = """ 
menu:
1. agregar estudiante
2. agregar curso
3. inscribir estudiante en curso
4. eliminar estudiante de curso
5. salir
"""

while True:
    print(menu)
    opcion = input("ingrese una opcion: ")
    
    if opcion == "1":
            nombre = input("Ingrese el nombre del estudiante: ")
            apellido = input("Ingrese el apellido del estudiante: ")
            estudiante = Estudiante(nombre, apellido)
            estudiantes.append(estudiante)
            print(f"Se ha agregado al estudiante: {estudiante.nombre} {estudiante.apellido}")

    elif opcion == "2":
            nombre = input("Ingrese el nombre del curso: ")
            descripcion = input("Ingrese la descripción del curso: ")
            curso = Curso(nombre, descripcion)
            cursos.append(curso)
            print(f"Se ha agregado el curso: {curso.nombre}")

    elif opcion == "3":
            print("\nEstudiantes:")
            for i, estudiante in enumerate(estudiantes):
                print(f"{i + 1}. {estudiante.nombre} {estudiante.apellido}")
            estudiante_idx = int(input("Seleccione un estudiante por su número: ")) - 1

            print("\nCursos:")
            for i, curso in enumerate(cursos):
                print(f"{i + 1}. {curso.nombre}")
            curso_idx = int(input("Seleccione un curso por su número: ")) - 1

            estudiantes[estudiante_idx].inscribir_curso(cursos[curso_idx])

    elif opcion == "4":
            print("\nEstudiantes:")
            for i, estudiante in enumerate(estudiantes):
                print(f"{i + 1}. {estudiante.nombre} {estudiante.apellido}")
            estudiante_idx = int(input("Seleccione un estudiante por su número: ")) - 1

            print("\nCursos en los que está inscrito el estudiante:")
            estudiante = estudiantes[estudiante_idx]
            for i, curso in enumerate(estudiante.cursos_inscritos):
                print(f"{i + 1}. {curso.nombre}")
            curso_idx = int(input("Seleccione un curso por su número para desinscribir al estudiante: ")) - 1

            estudiante.desinscribir_curso(estudiante.cursos_inscritos[curso_idx])

    elif opcion == "5":
            break
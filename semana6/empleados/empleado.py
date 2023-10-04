class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def describir_rol(self):
        print("Soy un empleado.")


class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def describir_rol(self):
        print(f"Soy gerente del departamento {self.departamento}.")


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def describir_rol(self):
        print(f"Soy un ingeniero {self.especialidad}.")


class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, supervisor):
        super().__init__(nombre, edad, salario)
        self.supervisor = supervisor

    def describir_rol(self):
        print(f"Soy un asistente bajo la supervisión de {self.supervisor}.")


empleados = []

while True:
    print("¿Qué tipo de empleado deseas crear? (empleado, gerente, ingeniero, asistente) o 'salir' para salir.")
    opcion = input().lower()

    if opcion == 'salir':
        break

    nombre = input("Nombre del empleado: ")
    edad = int(input("Edad del empleado: "))
    salario = float(input("Salario del empleado: "))

    if opcion == 'empleado':
        empleado = Empleado(nombre, edad, salario)
    elif opcion == 'gerente':
        departamento = input("Departamento del gerente: ")
        empleado = Gerente(nombre, edad, salario, departamento)
    elif opcion == 'ingeniero':
        especialidad = input("Especialidad del ingeniero: ")
        empleado = Ingeniero(nombre, edad, salario, especialidad)
    elif opcion == 'asistente':
        supervisor = input("Supervisor del asistente: ")
        empleado = Asistente(nombre, edad, salario, supervisor)
    else:
        print("Tipo de empleado no reconocido")
        continue

    empleados.append(empleado)
    empleado.describir_rol()


print("\nLista de empleados:")
for empleado in empleados:
    print(f"Nombre: {empleado.nombre}, Edad: {empleado.edad}, Salario: {empleado.salario}")

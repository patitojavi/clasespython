
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        print(
            f"nombre: {self.nombre}\nprecio: {self.precio}\ncategoría: {self.categoria}")


class Electronico(Producto):
    def __init__(self, nombre, precio, categoria, marca, modelo):
        super().__init__(nombre, precio, categoria)
        self.marca = marca
        self.modelo = modelo

    def mostrar_detalle(self):
        detalle_base = super().mostrar_detalle()
        print(f"{detalle_base}\nmarca: {self.marca}\nmodelo: {self.modelo}")


class Alimenticio(Producto):
    def __init__(self, nombre, precio, categoria, fecha_vencimiento):
        super().__init__(nombre, precio, categoria)
        self.fecha_vencimiento = fecha_vencimiento

    def mostrar_detalle(self):
        detalle_base = super().mostrar_detalle()
        print(f"{detalle_base}\nfecha de vencimiento: {self.fecha_vencimiento}")


class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, talla, color):
        super().__init__(nombre, precio, categoria)
        self.talla = talla
        self.color = color

    def mostrar_detalle(self):
        detalle_base = super().mostrar_detalle()
        print(f"{detalle_base}\ntalla: {self.talla}\ncolor: {self.color}")



productos_electronicos = []
productos_alimenticios = []
prendas_vestir = []

while True:
    print("Seleccione una opción:")
    print("1. Producto Electrónico")
    print("2. Producto Alimenticio")
    print("3. Prenda de Vestir")
    print("4. Mostrar productos guardados")
    print("5. Salir")
    
    opcion = input("Elija una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto electrónico: ")
        precio = float(input("Ingrese el precio del producto electrónico: "))
        categoria = input("Ingrese la categoría del producto electrónico: ")
        marca = input("Ingrese la marca del producto electrónico: ")
        modelo = input("Ingrese el modelo del producto electrónico: ")

        producto = Electronico(nombre, precio, categoria, marca, modelo)
        productos_electronicos.append(producto)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto alimenticio: ")
        precio = float(input("Ingrese el precio del producto alimenticio: "))
        categoria = input("Ingrese la categoría del producto alimenticio: ")
        fecha_vencimiento = input("Ingrese la fecha de vencimiento del producto alimenticio: ")

        producto = Alimenticio(nombre, precio, categoria, fecha_vencimiento)
        productos_alimenticios.append(producto)

    elif opcion == "3":
        nombre = input("Ingrese el nombre de la prenda de vestir: ")
        precio = float(input("Ingrese el precio de la prenda de vestir: "))
        categoria = input("Ingrese la categoría de la prenda de vestir: ")
        talla = input("Ingrese la talla de la prenda de vestir: ")
        color = input("Ingrese el color de la prenda de vestir: ")

        producto = Vestimenta(nombre, precio, categoria, talla, color)
        prendas_vestir.append(producto)

    elif opcion == "4":
        print("\nProductos Electrónicos:")
        for producto in productos_electronicos:
            producto.mostrar_detalle()
            print("--------------------")

        print("\nProductos Alimenticios:")
        for producto in productos_alimenticios:
            producto.mostrar_detalle()
            print("--------------------")

        print("\nPrendas de Vestir:")
        for producto in prendas_vestir:
            producto.mostrar_detalle()
            print("--------------------")

    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")

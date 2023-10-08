class Electrodomestico:
    def __init__(self, nombre, precio, garantiam):
        self.nombre = nombre
        self.precio = precio
        self.garantiam = garantiam

    def __str__(self):
        return f"{self.nombre}, Precio: ${self.precio}, Garantía: {self.garantiam} meses"


class Tienda:
    def __init__(self):
        self.inventario = []

    def agregar_producto(self, producto):
        self.inventario.append(producto)
        print(f"Se ha agregado el producto: {producto.nombre}")

    def buscar_producto(self, nombre):
        for producto in self.inventario:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def vender_producto(self, nombre):
        producto = self.buscar_producto(nombre)
        if producto:
            self.inventario.remove(producto)
            print(f"Se ha vendido el producto: {producto.nombre}")
        else:
            print(f"No se encontró el producto: {nombre}")

    def mostrar_inventario(self):
        print("\nInventario de la tienda:")
        for producto in self.inventario:
            print(producto)


tienda = Tienda()
menu = """Menú:"
    1. Agregar producto
    2. Buscar producto
    3. Vender producto
    4. Mostrar inventario
    5. Salir"""

while True:
    print(menu)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        garantia = int(input("Ingrese la garantía en meses: "))
        producto = Electrodomestico(nombre, precio, garantia)
        tienda.agregar_producto(producto)

    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto a buscar: ")
        encontrado = tienda.buscar_producto(nombre)
        if encontrado:
            print(f"Producto encontrado: {encontrado}")
        else:
            print(f"Producto no encontrado: {nombre}")

    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a vender: ")
        tienda.vender_producto(nombre)

    elif opcion == "4":
        tienda.mostrar_inventario()

    elif opcion == "5":
        break

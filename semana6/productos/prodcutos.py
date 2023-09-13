
class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        print(f"nombre: {self.nombre}\nprecio: {self.precio}\ncategoría: {self.categoria}")

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
#include <iostream>
#include <vector>
#include <string>

class Producto {
public:
    Producto(std::string nombre, float precio, std::string categoria)
        : nombre(nombre), precio(precio), categoria(categoria) {}

    void mostrar_detalle() {
        std::cout << "nombre: " << nombre << "\nprecio: " << precio << "\ncategoría: " << categoria << std::endl;
    }

private:
    std::string nombre;
    float precio;
    std::string categoria;
};

class Electronico : public Producto {
public:
    Electronico(std::string nombre, float precio, std::string categoria, std::string marca, std::string modelo)
        : Producto(nombre, precio, categoria), marca(marca), modelo(modelo) {}

    void mostrar_detalle() override {
        Producto::mostrar_detalle();
        std::cout << "marca: " << marca << "\nmodelo: " << modelo << std::endl;
    }

private:
    std::string marca;
    std::string modelo;
};

class Alimenticio : public Producto {
public:
    Alimenticio(std::string nombre, float precio, std::string categoria, std::string fecha_vencimiento)
        : Producto(nombre, precio, categoria), fecha_vencimiento(fecha_vencimiento) {}

    void mostrar_detalle() override {
        Producto::mostrar_detalle();
        std::cout << "fecha de vencimiento: " << fecha_vencimiento << std::endl;
    }

private:
    std::string fecha_vencimiento;
};

class Vestimenta : public Producto {
public:
    Vestimenta(std::string nombre, float precio, std::string categoria, std::string talla, std::string color)
        : Producto(nombre, precio, categoria), talla(talla), color(color) {}

    void mostrar_detalle() override {
        Producto::mostrar_detalle();
        std::cout << "talla: " << talla << "\ncolor: " << color << std::endl;
    }

private:
    std::string talla;
    std::string color;
};

int main() {
    std::vector<Producto*> productos_electronicos;
    std::vector<Producto*> productos_alimenticios;
    std::vector<Producto*> prendas_vestir;

    while (true) {
        std::cout << "Seleccione una opción:" << std::endl;
        std::cout << "1. Producto Electrónico" << std::endl;
        std::cout << "2. Producto Alimenticio" << std::endl;
        std::cout << "3. Prenda de Vestir" << std::endl;
        std::cout << "4. Mostrar productos guardados" << std::endl;
        std::cout << "5. Salir" << std::endl;

        std::string opcion;
        std::cin >> opcion;

        if (opcion == "1") {
            std::string nombre, categoria, marca, modelo;
            float precio;
            std::cout << "Ingrese el nombre del producto electrónico: ";
            std::cin >> nombre;
            std::cout << "Ingrese el precio del producto electrónico: ";
            std::cin >> precio;
            std::cout << "Ingrese la categoría del producto electrónico: ";
            std::cin >> categoria;
            std::cout << "Ingrese la marca del producto electrónico: ";
            std::cin >> marca;
            std::cout << "Ingrese el modelo del producto electrónico: ";
            std::cin >> modelo;

            Producto* producto = new Electronico(nombre, precio, categoria, marca, modelo);
            productos_electronicos.push_back(producto);
        } else if (opcion == "2") {
            std::string nombre, categoria, fecha_vencimiento;
            float precio;
            std::cout << "Ingrese el nombre del producto alimenticio: ";
            std::cin >> nombre;
            std::cout << "Ingrese el precio del producto alimenticio: ";
            std::cin >> precio;
            std::cout << "Ingrese la categoría del producto alimenticio: ";
            std::cin >> categoria;
            std::cout << "Ingrese la fecha de vencimiento del producto alimenticio: ";
            std::cin >> fecha_vencimiento;

            Producto* producto = new Alimenticio(nombre, precio, categoria, fecha_vencimiento);
            productos_alimenticios.push_back(producto);
        } else if (opcion == "3") {
            std::string nombre, categoria, talla, color;
            float precio;
            std::cout << "Ingrese el nombre de la prenda de vestir: ";
            std::cin >> nombre;
            std::cout << "Ingrese el precio de la prenda de vestir: ";
            std::cin >> precio;
            std::cout << "Ingrese la categoría de la prenda de vestir: ";
            std::cin >> categoria;
            std::cout << "Ingrese la talla de la prenda de vestir: ";
            std::cin >> talla;
            std::cout << "Ingrese el color de la prenda de vestir: ";
            std::cin >> color;

            Producto* producto = new Vestimenta(nombre, precio, categoria, talla, color);
            prendas_vestir.push_back(producto);
        } else if (opcion == "4") {
            std::cout << "\nProductos Electrónicos:" << std::endl;
            for (Producto* producto : productos_electronicos) {
                producto->mostrar_detalle();
                std::cout << "--------------------" << std::endl;
            }

            std::cout << "\nProductos Alimenticios:" << std::endl;
            for (Producto* producto : productos_alimenticios) {
                producto->mostrar_detalle();
                std::cout << "--------------------" << std::endl;
            }

            std::cout << "\nPrendas de Vestir:" << std::endl;
            for (Producto* producto : prendas_vestir) {
                producto->mostrar_detalle();
                std::cout << "--------------------" << std::endl;
            }
        } else if (opcion == "5") {
            // Liberar la memoria de los productos
            for (Producto* producto : productos_electronicos) {
                delete producto;
            }
            for (Producto* producto : productos_alimenticios) {
                delete producto;
            }
            for (Producto* producto : prendas_vestir) {
                delete producto;
            }
            break;
        } else {
            std::cout << "Opción no válida. Por favor, elija una opción válida." << std::endl;
        }
    }

    return 0;
}

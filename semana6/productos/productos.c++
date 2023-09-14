#include <iostream>
#include <string>

class Producto {
public:
    Producto(const std::string& nombre, double precio, const std::string& categoria)
        : nombre(nombre), precio(precio), categoria(categoria) {}

    void mostrar_detalle() {
        std::cout << "nombre: " << nombre << "\nprecio: " << precio << "\ncategoría: " << categoria << std::endl;
    }

private:
    std::string nombre;
    double precio;
    std::string categoria;
};
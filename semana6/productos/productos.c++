#include <iostream>
#include <string>

class Producto {
public:
    Producto(const std::string& nombre, float precio, const std::string& categoria)
        : nombre(nombre), precio(precio), categoria(categoria) {}

    void mostrarDetalle() {
        std::cout << "nombre: " << nombre << "\nprecio: " << precio << "\ncategoría: " << categoria << std::endl;
    }

private:
    std::string nombre;
    float precio;
    std::string categoria;
};

class Electronico : public Producto {
public:
    Electronico(const std::string& nombre, float precio, const std::string& categoria,
                const std::string& marca, const std::string& modelo)
        : Producto(nombre, precio, categoria), marca(marca), modelo(modelo) {}

    void mostrarDetalle() {
        Producto::mostrarDetalle();
        std::cout << "marca: " << marca << "\nmodelo: " << modelo << std::endl;
    }

private:
    std::string marca;
    std::string modelo;
};

class Alimenticio : public Producto {
public:
    Alimenticio(const std::string& nombre, float precio, const std::string& categoria,
                const std::string& fechaVencimiento)
        : Producto(nombre, precio, categoria), fechaVencimiento(fechaVencimiento) {}

    void mostrarDetalle() {
        Producto::mostrarDetalle();
        std::cout << "fecha de vencimiento: " << fechaVencimiento << std::endl;
    }

private:
    std::string fechaVencimiento;
};

class Vestimenta : public Producto {
public:
    Vestimenta(const std::string& nombre, float precio, const std::string& categoria,
            const std::string& talla, const std::string& color)
        : Producto(nombre, precio, categoria), talla(talla), color(color) {}

    void mostrarDetalle() {
        Producto::mostrarDetalle();
        std::cout << "talla: " << talla << "\ncolor: " << color << std::endl;
    }

private:
    std::string talla;
    std::string color;
};


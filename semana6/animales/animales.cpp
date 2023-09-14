#include <iostream>
#include <string>



class Animal {
public:
    Animal(const std::string& nombre, int edad)
        : nombre(nombre), edad(edad) {}

    virtual std::string sonido() const {
        return "";
    }

    std::string getNombre() const {
        return nombre;
    }

    int getEdad() const {
        return edad;
    }

private:
    std::string nombre;
    int edad;
};



class Perro : public Animal {
public:
    Perro(const std::string& nombre, int edad)
        : Animal(nombre, edad) {}

    std::string sonido() const override {
        return "guau";
    }
};



class Gato : public Animal {
public:
    Gato(const std::string& nombre, int edad)
        : Animal(nombre, edad) {}

    std::string sonido() const override {
        return "miau";
    }
};



class Pajaro : public Animal {
public:
    Pajaro(const std::string& nombre, int edad)
        : Animal(nombre, edad) {}

    std::string sonido() const override {
        return "pio";
    }
};
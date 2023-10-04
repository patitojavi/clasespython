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



int main() {
    while (true) {
        std::cout << "¿Qué animal quieres escuchar? (perro, gato, pajaro) o 'salir' para salir." << std::endl;
        std::string opcion;
        std::cin >> opcion;

        if (opcion == "salir") {
            break;
        }

        Animal* animal = nullptr;
        if (opcion == "perro") {
            animal = new Perro("Eduardo", 3);
        } else if (opcion == "gato") {
            animal = new Gato("Javi", 2);
        } else if (opcion == "pajaro") {
            animal = new Pajaro("Pato", 1);
        } else {
            std::cout << "Animal no reconocido" << std::endl;
            continue;
        }

        std::cout << animal->nombre << " hace el sonido: " << animal->sonido() << std::endl;

        delete animal;
    }

    return 0;
}
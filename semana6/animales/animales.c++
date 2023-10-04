#include <iostream>
#include <vector>

class Animal {
public:
    Animal(std::string nombre, int edad) : nombre(nombre), edad(edad) {}
    virtual std::string sonido() = 0;

protected:
    std::string nombre;
    int edad;
};

class Perro : public Animal {
public:
    Perro(std::string nombre, int edad) : Animal(nombre, edad) {}
    std::string sonido() override {
        return "guau";
    }
};

class Gato : public Animal {
public:
    Gato(std::string nombre, int edad) : Animal(nombre, edad) {}
    std::string sonido() override {
        return "miau";
    }
};

class Pajaro : public Animal {
public:
    Pajaro(std::string nombre, int edad) : Animal(nombre, edad) {}
    std::string sonido() override {
        return "pio";
    }
};

int main() {
    std::vector<Animal*> animales;

    while (true) {
        std::cout << "Seleccione una opción:" << std::endl;
        std::cout << "1. Agregar Perro" << std::endl;
        std::cout << "2. Agregar Gato" << std::endl;
        std::cout << "3. Agregar Pájaro" << std::endl;
        std::cout << "4. Mostrar Animales" << std::endl;
        std::cout << "5. Salir" << std::endl;

        std::string opcion;
        std::cin >> opcion;

        if (opcion == "1") {
            std::string nombre;
            int edad;
            std::cout << "Ingrese el nombre del perro: ";
            std::cin >> nombre;
            std::cout << "Ingrese la edad del perro: ";
            std::cin >> edad;
            Perro* perro = new Perro(nombre, edad);
            animales.push_back(perro);
        } else if (opcion == "2") {
            std::string nombre;
            int edad;
            std::cout << "Ingrese el nombre del gato: ";
            std::cin >> nombre;
            std::cout << "Ingrese la edad del gato: ";
            std::cin >> edad;
            Gato* gato = new Gato(nombre, edad);
            animales.push_back(gato);
        } else if (opcion == "3") {
            std::string nombre;
            int edad;
            std::cout << "Ingrese el nombre del pájaro: ";
            std::cin >> nombre;
            std::cout << "Ingrese la edad del pájaro: ";
            std::cin >> edad;
            Pajaro* pajaro = new Pajaro(nombre, edad);
            animales.push_back(pajaro);
        } else if (opcion == "4") {
            std::cout << "\nListado de Animales:" << std::endl;
            for (Animal* animal : animales) {
                std::cout << "Nombre: " << animal->nombre << ", Edad: " << animal->edad << ", Sonido: " << animal->sonido() << std::endl;
                std::cout << "--------------------" << std::endl;
            }
        } else if (opcion == "5") {
            // Liberar la memoria de los objetos
            for (Animal* animal : animales) {
                delete animal;
            }
            break;
        } else {
            std::cout << "Opción no válida. Por favor, elija una opción válida." << std::endl;
        }
    }

    return 0;
}

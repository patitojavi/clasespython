#include <iostream>
#include <vector>
#include <string>

class Empleado {
public:
    Empleado(std::string nombre, int edad, float salario) : nombre(nombre), edad(edad), salario(salario) {}

    virtual void describir_rol() {
        std::cout << "Soy un empleado." << std::endl;
    }

protected:
    std::string nombre;
    int edad;
    float salario;
};

class Gerente : public Empleado {
public:
    Gerente(std::string nombre, int edad, float salario, std::string departamento) : Empleado(nombre, edad, salario), departamento(departamento) {}

    void describir_rol() override {
        std::cout << "Soy gerente del departamento " << departamento << "." << std::endl;
    }

private:
    std::string departamento;
};

class Ingeniero : public Empleado {
public:
    Ingeniero(std::string nombre, int edad, float salario, std::string especialidad) : Empleado(nombre, edad, salario), especialidad(especialidad) {}

    void describir_rol() override {
        std::cout << "Soy un ingeniero " << especialidad << "." << std::endl;
    }

private:
    std::string especialidad;
};

class Asistente : public Empleado {
public:
    Asistente(std::string nombre, int edad, float salario, std::string supervisor) : Empleado(nombre, edad, salario), supervisor(supervisor) {}

    void describir_rol() override {
        std::cout << "Soy un asistente bajo la supervisión de " << supervisor << "." << std::endl;
    }

private:
    std::string supervisor;
};

int main() {
    std::vector<Empleado*> empleados;

    while (true) {
        std::cout << "¿Qué tipo de empleado deseas crear? (empleado, gerente, ingeniero, asistente) o 'salir' para salir." << std::endl;
        std::string opcion;
        std::cin >> opcion;

        if (opcion == "salir") {
            break;
        }

        std::string nombre;
        int edad;
        float salario;

        std::cout << "Nombre del empleado: ";
        std::cin >> nombre;
        std::cout << "Edad del empleado: ";
        std::cin >> edad;
        std::cout << "Salario del empleado: ";
        std::cin >> salario;

        Empleado* empleado;

        if (opcion == "empleado") {
            empleado = new Empleado(nombre, edad, salario);
        } else if (opcion == "gerente") {
            std::string departamento;
            std::cout << "Departamento del gerente: ";
            std::cin >> departamento;
            empleado = new Gerente(nombre, edad, salario, departamento);
        } else if (opcion == "ingeniero") {
            std::string especialidad;
            std::cout << "Especialidad del ingeniero: ";
            std::cin >> especialidad;
            empleado = new Ingeniero(nombre, edad, salario, especialidad);
        } else if (opcion == "asistente") {
            std::string supervisor;
            std::cout << "Supervisor del asistente: ";
            std::cin >> supervisor;
            empleado = new Asistente(nombre, edad, salario, supervisor);
        } else {
            std::cout << "Tipo de empleado no reconocido" << std::endl;
            continue;
        }

        empleados.push_back(empleado);
        empleado->describir_rol();
    }

    std::cout << "\nLista de empleados:" << std::endl;
    for (Empleado* empleado : empleados) {
        std::cout << "Nombre: " << empleado->nombre << ", Edad: " << empleado->edad << ", Salario: " << empleado->salario << std::endl;
        delete empleado;  // Liberar la memoria
    }

    return 0;
}

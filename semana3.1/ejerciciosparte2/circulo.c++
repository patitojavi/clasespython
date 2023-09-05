#include <iostream>

class Circulo {
private:
    double radio;

public:
    Circulo(double _radio) : radio(_radio) {}

    double calcularArea() {
        const double numeropi = 3.14;
        return numeropi * radio * radio;
    }

    double calcularPerimetro() {
        const double numeropi = 3.14;
        return 2 * numeropi * radio;
    }
};

int main() {
    double radio;

    std::cout << "Dame el radio del círculo: ";
    std::cin >> radio;

    Circulo circulo(radio);

    std::cout << "El área del círculo es: " << circulo.calcularArea() << std::endl;
    std::cout << "El perímetro del círculo es: " << circulo.calcularPerimetro() << std::endl;

    return 0;
}
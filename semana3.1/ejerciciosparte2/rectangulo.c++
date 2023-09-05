#include <iostream>

class Rectangulo {
private:
    double longitud;
    double ancho;

public:
    Rectangulo(double _longitud, double _ancho) : longitud(_longitud), ancho(_ancho) {}

    double calcularArea() {
        return longitud * ancho;
    }

    double calcularPerimetro() {
        return 2 * (longitud + ancho);
    }
};

int main() {
    double longitud, ancho;
    
    std::cout << "Dame la longitud del rectángulo: ";
    std::cin >> longitud;
    
    std::cout << "Dame el ancho del rectángulo: ";
    std::cin >> ancho;

    Rectangulo rectangulo(longitud, ancho);

    std::cout << "El área del rectángulo es: " << rectangulo.calcularArea() << std::endl;
    std::cout << "El perímetro del rectángulo es: " << rectangulo.calcularPerimetro() << std::endl;

    return 0;
}
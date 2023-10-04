#include <iostream>
#include <vector>
#include <string>

class Reserva {
public:
    Reserva(std::string pasajero, std::string vuelo, std::string fecha)
        : pasajero(pasajero), vuelo(vuelo), fecha(fecha) {}

    virtual void mostrar_detalle() {
        // Dejar vacío ya que no se especifica cómo mostrar la reserva
    }

protected:
    std::string pasajero;
    std::string vuelo;
    std::string fecha;
};

class ReservaEconomica : public Reserva {
public:
    ReservaEconomica(std::string pasajero, std::string vuelo, std::string fecha, std::string asiento)
        : Reserva(pasajero, vuelo, fecha), asiento(asiento) {}

    void mostrar_detalle() override {
        std::cout << "Reserva Económica - Pasajero: " << pasajero << ", Vuelo: " << vuelo << ", Fecha: " << fecha << ", Asiento: " << asiento << std::endl;
    }

private:
    std::string asiento;
};

class ReservaBusiness : public Reserva {
public:
    ReservaBusiness(std::string pasajero, std::string vuelo, std::string fecha, std::string asiento_negocio)
        : Reserva(pasajero, vuelo, fecha), asiento_negocio(asiento_negocio) {}

    void mostrar_detalle() override {
        std::cout << "Reserva Business - Pasajero: " << pasajero << ", Vuelo: " << vuelo << ", Fecha: " << fecha << ", Asiento Negocio: " << asiento_negocio << std::endl;
    }

private:
    std::string asiento_negocio;
};

class ReservaPrimeraClase : public Reserva {
public:
    ReservaPrimeraClase(std::string pasajero, std::string vuelo, std::string fecha, std::string asientovip)
        : Reserva(pasajero, vuelo, fecha), asientovip(asientovip) {}

    void mostrar_detalle() override {
        std::cout << "Reserva Primera Clase - Pasajero: " << pasajero << ", Vuelo: " << vuelo << ", Fecha: " << fecha << ", Asiento VIP: " << asientovip << std::endl;
    }

private:
    std::string asientovip;
};

int main() {
    std::vector<Reserva*> reservas;

    while (true) {
        std::string pasajero, vuelo, fecha;
        std::cout << "Nombre del pasajero: ";
        std::cin >> pasajero;
        std::cout << "Número de vuelo: ";
        std::cin >> vuelo;
        std::cout << "Fecha de vuelo: ";
        std::cin >> fecha;

        std::string tipo_reserva;
        std::cout << "Tipo de reserva (Economica/Business/PrimeraClase): ";
        std::cin >> tipo_reserva;

        Reserva* reserva;

        if (tipo_reserva == "economica") {
            std::string asiento;
            std::cout << "Número de asiento: ";
            std::cin >> asiento;
            reserva = new ReservaEconomica(pasajero, vuelo, fecha, asiento);
        } else if (tipo_reserva == "business") {
            std::string asiento_negocio;
            std::cout << "Número de asiento de negocios: ";
            std::cin >> asiento_negocio;
            reserva = new ReservaBusiness(pasajero, vuelo, fecha, asiento_negocio);
        } else if (tipo_reserva == "primerclase") {
            std::string asientovip;
            std::cout << "Número de asiento VIP: ";
            std::cin >> asientovip;
            reserva = new ReservaPrimeraClase(pasajero, vuelo, fecha, asientovip);
        } else {
            std::cout << "Tipo de reserva no válido. Inténtalo de nuevo." << std::endl;
            continue;
        }

        reservas.push_back(reserva);

        std::string otra_reserva;
        std::cout << "¿Deseas hacer otra reserva? (si/no): ";
        std::cin >> otra_reserva;
        if (otra_reserva != "si") {
            break;
        }
    }

    std::cout << "\nReservas:" << std::endl;
    for (Reserva* reserva : reservas) {
        reserva->mostrar_detalle();
        delete reserva; // Liberar la memoria
    }

    return 0;
}

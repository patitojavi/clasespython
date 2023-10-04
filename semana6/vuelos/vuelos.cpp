#include <iostream>
#include <string>



class Reserva {
public:
    Reserva(const std::string& pasajero, const std::string& vuelo, const std::string& fecha)
        : pasajero(pasajero), vuelo(vuelo), fecha(fecha) {}

    virtual void mostrar_detalle() const {
    }

protected:
    std::string pasajero;
    std::string vuelo;
    std::string fecha;
};

class ReservaEconomica : public Reserva {
public:
    ReservaEconomica(const std::string& pasajero, const std::string& vuelo, const std::string& fecha, const std::string& asiento)
        : Reserva(pasajero, vuelo, fecha), asiento(asiento) {}

    void mostrar_detalle() const override {
        std::cout << "Reserva Económica - Pasajero: " << pasajero << ", Vuelo: " << vuelo << ", Fecha: " << fecha << ", Asiento: " << asiento << std::endl;
    }

private:
    std::string asiento;
};

class ReservaBusiness : public Reserva {
public:
    ReservaBusiness(const std::string& pasajero, const std::string& vuelo, const std::string& fecha, const std::string& asiento_negocio)
        : Reserva(pasajero, vuelo, fecha), asiento_negocio(asiento_negocio) {}

    void mostrar_detalle() const override {
        std::cout << "Reserva Business - Pasajero: " << pasajero << ", Vuelo: " << vuelo << ", Fecha: " << fecha << ", Asiento Negocio: " << asiento_negocio << std::endl;
    }

private:
    std::string asiento_negocio;
};

class ReservaPrimeraClase : public Reserva {
public:
    ReservaPrimeraClase(const std::string& pasajero, const std::string& vuelo, const std::string& fecha, const std::string& asiento_vip)
        : Reserva(pasajero, vuelo, fecha), asiento_vip(asiento_vip) {}

    void mostrar_detalle() const override {
        std::cout << "Reserva Primera Clase - Pasajero: " << pasajero << ", Vuelo: " << vuelo << ", Fecha: " << fecha << ", Asiento VIP: " << asiento_vip << std::endl;
    }

private:
    std::string asiento_vip;
};
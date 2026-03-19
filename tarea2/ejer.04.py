class Bus:

    def __init__(self, AsientosTotales):
        self.AsientosTotales = AsientosTotales
        self.Pasajeros = 0

    def subirPasajeros(self, x):
        if self.Pasajeros + x <= self.AsientosTotales:
            self.Pasajeros += x
        else:
            print("No hay asientos disponibles")
    def cobrarPasaje(self):
        return self.Pasajeros * 1.50

    def asientosDisponibles(self):
        return self.AsientosTotales - self.Pasajeros

    def __str__(self):
        return "Bus[{},{}]".format(self.Pasajeros, self.asientosDisponibles())

class Main():
    bus = Bus(100)

    bus.subirPasajeros(25)
    
    print(bus)
    print("Total de pasajeros que subieron: {}".format(bus.Pasajeros))
    print("Total de pasaje recaudado: bs {}".format(bus.cobrarPasaje()))
    print("Asientos disponibles: {}".format(bus.asientosDisponibles()))
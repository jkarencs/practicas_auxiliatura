from multimethod import multimethod

class Videojuego:

    @multimethod
    def __init__(self, nombre: str, plataforma: str, jugadores: int):
        self.__nombre = nombre
        self.__plataforma = plataforma
        self.__cantidadJugadores = jugadores

    @multimethod
    def __init__(self, nombre: str, plataforma: str):
        self.__nombre = nombre
        self.__plataforma = plataforma
        self.__cantidadJugadores = 1

    @multimethod
    def agregarJugadores(self):
        self.__cantidadJugadores += 1

    @multimethod
    def agregarJugadores(self, n: int):
        self.__cantidadJugadores += n

    def __str__(self):
        return "[{}, {}, {}]".format(self.__nombre, self.__plataforma, self.__cantidadJugadores)


v1 = Videojuego("Vice City", "PS2", 2)
v2 = Videojuego("Minecraft", "PC")

print(v1)
print(v2)

v1.agregarJugadores()
print(v1)
v2.agregarJugadores(int(input()))
print(v2)
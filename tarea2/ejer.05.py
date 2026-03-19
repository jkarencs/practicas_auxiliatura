class Minecraft:
    def __init__(self):
        self.__jugadores = []
        self.__diamantes = []

    def addJugador(self, jugador, diamantes):
        if len(self.__jugadores) < 10:
            self.__jugadores.append(jugador)
            self.__diamantes.append(diamantes)
        else:
            print("Servidor lleno")

    def VerificarStacksDiamantes(self):
        for i in range(len(self.__jugadores)):
            stacks = self.__diamantes[i] // 64
            print("{} tiene {} stack de diamantes".format(self.__jugadores[i], stacks))

    def MayorDiamantes(self):
        MayorDiamantes = -1
        nombre = ""
        for i in range(len(self.__jugadores)):
            if self.__diamantes[i] > MayorDiamantes:
                MayorDiamantes = self.__diamantes[i]
                nombre = self.__jugadores[i]
        print("Jugador con más diamantes: {}".format(nombre))

    def totalDiamantes(self):
        total = sum(self.__diamantes)
        print("Total diamantes:", total)

class Main():

    servidor = Minecraft()
    
    servidor.addJugador("Jane", 128)
    servidor.addJugador("John", 256)
    servidor.addJugador("Doris", 64)
    servidor.addJugador("Alice", 192)
    servidor.addJugador("David", 32)
    servidor.addJugador("Camila", 160)
    servidor.addJugador("Adrie", 48)
    servidor.addJugador("Edi", 80)
    servidor.addJugador("July", 16)
    servidor.addJugador("Madison", 224)     

    
    servidor.VerificarStacksDiamantes()
    print("--------------------------------")
    servidor.MayorDiamantes()
    servidor.totalDiamantes()
# Mascotas.py (Heredan de Animal)
from Animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueño, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueño) # Llama al padre
        self.__requiereBosal = requiereBosal
        self.__ladraFuerte = ladraFuerte

class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueño, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, nombreDueño)
        self.__cazaRatones = cazaRatones
        self.__tomaLeche = tomaLeche
    def getTomaLeche(self): return self.__tomaLeche
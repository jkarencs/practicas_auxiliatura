# Animal.py
class Animal:
    def __init__(self, nombre, edad, nombreDueño):
        self._nombre = nombre
        self._edad = edad
        self._nombreDueño = nombreDueño

    def getEdad(self): return self._edad
    def getDueño(self): return self._nombreDueño
    def getNombre(self): return self._nombre


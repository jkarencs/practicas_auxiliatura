from multimethod import multimethod

class Aula:

    def __init__(self, nombreAula, piso, estudiantes):
        self.__nombreAula = nombreAula
        self.__piso = piso
        self.__estudiantes = estudiantes

    @multimethod
    def mostrar(self):
        print("Aula:", self.__nombreAula)
        print("Piso:", self.__piso)
        print("Estudiantes:")
        for estudiante in self.__estudiantes:
            print(estudiante[0], estudiante[1])

    @multimethod
    def mostrar(self, opcion: int):
        for estudiante in self.__estudiantes:
            if estudiante[1] >= 51:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"
            print(estudiante[0], estudiante[1], estado)


est = [
    ["Juan", 43],
    ["Maria", 89]
]

A1 = Aula("Aula 101", 1, est)

A1.mostrar()
print()
A1.mostrar(1)
#biblioteca
class Biblioteca:
    def __init__(self,NomBiblio):
        self.__nombre=NomBiblio
        self.__cantidadLibros= 0
        self.__libros=[]

    def agregarLibro(self,l):
        if(len(self.__libros)<100):
            self.__libros.append(l)
            self.__cantidadLibros+=1
        else:
            print("No se pueden agregar más libros, la biblioteca está llena.")


    def buscarLibro(self, nombre_buscar):
        for libro in self.__libros:
            if libro.getNombre() == nombre_buscar:
                print(f"Encontrado: {libro}")
                return True
        print(f"El libro '{nombre_buscar}' no se encuentra en la biblioteca.")
        return False
    def getCantidad(self):
        return self.__cantidadLibros
    
    def __str__(self):
        return f"Biblioteca: {self.__nombre}, Cantidad de Libros: {self.__cantidadLibros}"

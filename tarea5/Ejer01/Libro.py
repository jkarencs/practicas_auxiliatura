#Carrillo Salinas Karen Jeanette 
#IV. agregacion/composicion
#Resolviendo ejercicios 1 y 5 de esta sección
  ##Ejercicio 1: Dado el siguiente diagrama(libro - biblioteca)
#a. Implementar las clases con sus constructores y métodos necesarios de la agregación.
#b. Instanciar 2 Bibliotecas, agregar al menos 2 libros a cada biblioteca
#c. Crear un método para verificar si el libro de nombre X está en la biblioteca, si lo está mostrar sus datos.
#d. Mostrar la biblioteca que contenga la mayor cantidad de libros, si hay empate debe mostrar ambas.

#libro
class Libro:
    def __init__(self,Nom,au,año):
        self.__nombre=Nom
        self.__autor=au
        self.__año= año
    def getNombre(self):
        return self.__nombre
    def getAutor(self):
        return self.__autor
    def getAño(self):
        return self.__año
    def __str__(self):
        return f"Nombre: {self.__nombre}, Autor: {self.__autor}, Año: {self.__año}" 
    

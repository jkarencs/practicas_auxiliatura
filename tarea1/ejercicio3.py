class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre          
        self.__material = material   
        self.__tipo = tipo          

    def getMaterial(self):
        return self.__material

    def getTipo(self):
        return self.__tipo

    def setMaterial(self, material):
        self.__material = material

    def setTipo(self, tipo):
        self.__tipo = tipo

    def __str__(self):
        return f"Instrumento: {self.nombre}, Material: {self.__material}, Tipo: {self.__tipo}"
    
if __name__ == "__main__":

    ins1 = Instrumento("Guitarra", "Madera", "Cuerda")
    ins2 = Instrumento("batería", "Metal", "Percusión")
    
    print("Datos de Instrumento")
    print(ins1)
    print(ins2)
    
    print(f"El material del segundo instrumento es: {ins2.getMaterial()}")
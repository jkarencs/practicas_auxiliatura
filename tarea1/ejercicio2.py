class Televisor:
    def __init__(self, marca="", resolucion=0, tipo=""):
        self.__marca = marca                
        self.__resolucion = resolucion      
        self.__tipo = tipo                  

    def getMarca(self): return self.__marca
    def getResolucion(self): return self.__resolucion
    def getTipo(self): return self.__tipo

    def setMarca(self, m): self.__marca = m
    def setResolucion(self, r): self.__resolucion = r
    def setTipo(self, t): self.__tipo = t

    def __str__(self):
        return f"Televisor[marca={self.__marca}, resolucion={self.__resolucion}, tipo={self.__tipo}]"
    
   
if __name__ == "__main__":
    
    tv1 = Televisor("Samsung", 4, "OLED")
    tv2 = Televisor("LG", 8, "IPS")
    
   
    print("Datos de Televisores:")
    print(tv1)
    print(tv2)
    
    tv1.setMarca("Sony")
    print(f"Marca actualizada de la primera TV: {tv1.getMarca()}")
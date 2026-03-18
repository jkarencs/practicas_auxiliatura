class Anime:
    def __init__(self, nombre, genero, nroEpisodios):
        self.nombre = nombre                
        self.genero = genero               
        self.__nroEpisodios = nroEpisodios 
        self.__episodios = []              

    def getNroEpisodios(self):
        return self.__nroEpisodios

    def setNroEpisodios(self, nro):
        self.__nroEpisodios = nro

    def __str__(self):
        return f"Anime[nombre={self.nombre}, genero={self.genero}, nroEpisodios={self.__nroEpisodios}]"
  
if __name__ == "__main__":

    anime1 = Anime("Dragon Ball", "Shonen", 153)
    anime2 = Anime("Candy Candy", "Shojo", 115)
    
    
    print("--- Datos de Anime ---")
    print(anime1)
    print(anime2)
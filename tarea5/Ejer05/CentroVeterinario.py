class CentroVeterinario:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__perros = []
        self.__gatos = []
        self.__cantPerros = 0
        self.__cantGatos = 0

    def agregarPerro(self, p):
        if len(self.__perros) < 100:
            self.__perros.append(p)
            self.__cantPerros += 1

    def agregarGato(self, g):
        if len(self.__gatos) < 100:
            self.__gatos.append(g)
            self.__cantGatos += 1

    def ordenarPerros(self):
        # Ordena por edad, luego dueño, luego nombre
        self.__perros.sort(key=lambda p: (p.getEdad(), p.getDueño(), p.getNombre()))
        print(f"Perros en {self.__nombre} ordenados.")

    def ordenarGatos(self):
        # Ordena: toma leche primero (not), edad mayor a menor (-), y nombre
        self.__gatos.sort(key=lambda g: (not g.getTomaLeche(), -g.getEdad(), g.getNombre()))
        print(f"Gatos en {self.__nombre} ordenados.")

    def verificarMismoDueño(self):
        todos = self.__perros + self.__gatos
        ya_mostrados = []
        for i in range(len(todos)):
            dueño = todos[i].getDueño()
            if dueño not in ya_mostrados:
                cont = 0
                for animal in todos:
                    if animal.getDueño() == dueño:
                        cont += 1
                if cont >= 2:
                    print(f"El dueño {dueño} tiene {cont} animales.")
                    ya_mostrados.append(dueño)

    def __str__(self):
        return f"Veterinaria: {self.__nombre}"
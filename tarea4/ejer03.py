# Dado el siguiente diagrama:
#a. Implementar las clases con sus respectivos constructores y método para mostrar.
#b.nstanciar 2 estudiantes y 1 docente, y mostrar sus datos.
#c.Verificar si algún estudiante tiene la misma edad que el docente.
#d.Crear un método para verificar si dos estudiantes están en la misma carrera
# -------------------------
# CLASE PADRE
# -------------------------
class Persona:
    def __init__(self, nombre, carnet, edad):
        self.nombre = nombre
        self.carnet = carnet
        self.edad = edad

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Carnet:", self.carnet)
        print("Edad:", self.edad)


#**************************
# CLASE HIJA: ESTUDIANTE
#**************************
class Estudiante(Persona):
    def __init__(self, nombre, carnet, edad, matricula, carrera):
        super().__init__(nombre, carnet, edad)
        self.matricula = matricula
        self.carrera = carrera

    def mostrar(self):
        super().mostrar()
        print("Matricula:", self.matricula)
        print("Carrera:", self.carrera)

    def misma_carrera(self, otro):
        if self.carrera == otro.carrera:
            return True
        else:
            return False


# -------------------------
# CLASE HIJA: DOCENTE
# -------------------------
class Docente(Persona):
    def __init__(self, nombre, carnet, edad, antiguedad, sueldo):
        super().__init__(nombre, carnet, edad)
        self.antiguedad = antiguedad
        self.sueldo = sueldo

    def mostrar(self):
        super().mostrar()
        print("Antiguedad:", self.antiguedad)
        print("Sueldo:", self.sueldo)


# -------------------------
# PROGRAMA PRINCIPAL
# -------------------------

# Crear objetos
est1 = Estudiante("Karen", 12345, 18, 1001, "Ingenieria en Sistemas")
est2 = Estudiante("Luis", 67890, 20, 1002, "Ingenieria Civil")
doc = Docente("Carlos", 11111, 20, 5, 3500.50)

print("\n--- ESTUDIANTE 1 ---")
est1.mostrar()

print("\n--- ESTUDIANTE 2 ---")
est2.mostrar()

print("\n--- DOCENTE ---")
doc.mostrar()

# Veriedad
if est1.edad == doc.edad:
    print("\nEl estudiante 1 tiene la misma edad que el docente")

if est2.edad == doc.edad:
    print("El estudiante 2 tiene la misma edad que el docente")

# Ver,carrera
if est1.misma_carrera(est2):
    print("\nAmbos estudiantes están en la misma carrera")
else:
    print("\nNo están en la misma carrera")
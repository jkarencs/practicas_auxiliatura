from Mascotas import Perro, Gato
from CentroVeterinario import CentroVeterinario

# 1. Crear los dos centros veterinarios
vete1 = CentroVeterinario("San Roque")
vete2 = CentroVeterinario("Vida Animal")

# 2. Crear mascotas para vete1
p1 = Perro("Rex", 5, "Karen", False, True)
p2 = Perro("Toby", 2, "Ana", True, False)
g1 = Gato("Michi", 3, "Karen", True, True)
g2 = Gato("Luna", 1, "Carlos", False, True)

vete1.agregarPerro(p1)
vete1.agregarPerro(p2)
vete1.agregarGato(g1)
vete1.agregarGato(g2)

# 3. Crear mascotas para vete2 (Inciso A pide al menos 2 y 2)
p3 = Perro("Apolo", 4, "Juan", False, False)
p4 = Perro("Bruno", 4, "Juan", True, True)
g3 = Gato("Pelusa", 6, "Maria", True, False)
g4 = Gato("Garfield", 8, "Maria", False, True)

vete2.agregarPerro(p3)
vete2.agregarPerro(p4)
vete2.agregarGato(g3)
vete2.agregarGato(g4)

# --- PRUEBAS VETERINARIA 1 ---
print(f"--- {vete1} ---")
vete1.ordenarPerros() 
vete1.ordenarGatos()  
vete1.verificarMismoDueño() 

print("-" * 20)

# --- PRUEBAS VETERINARIA 2 ---
print(f"--- {vete2} ---")
vete2.verificarMismoDueño() 
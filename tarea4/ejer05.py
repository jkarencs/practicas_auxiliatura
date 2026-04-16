from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def obtenerArea(self):
        pass

# CLASE CUADRADO
class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def obtenerArea(self):
        return self.lado * self.lado

    def mostrar(self):
        print("Cuadrado")
        print("Color:", self.color)
        print("Lado:", self.lado)
        print("Área:", self.obtenerArea())


# CLASE TRIANGULO
class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def obtenerArea(self):
        # Fórmula de Herón
        s = (self.lado1 + self.lado2 + self.lado3) / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return area

    def mostrar(self):
        print("Triángulo")
        print("Color:", self.color)
        print("Lados:", self.lado1, self.lado2, self.lado3)
        print("Área:", self.obtenerArea())


# CLASE REDONDO
class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def obtenerArea(self):
        return 3.1416 * self.radio * self.radio

    def mostrar(self):
        print("Redondo")
        print("Color:", self.color)
        print("Radio:", self.radio)
        print("Área:", self.obtenerArea())

# Crear objetos (2 de cada uno)
c1 = Cuadrado("Rojo", 4)
c2 = Cuadrado("Azul", 6)

t1 = Triangulo("Verde", 3, 4, 5)
t2 = Triangulo("Amarillo", 5, 5, 6)

r1 = Redondo("Negro", 3)
r2 = Redondo("Blanco", 5)

# Mostrar todos
print("\n--- CUADRADOS ---")
c1.mostrar()
c2.mostrar()

print("\n--- TRIANGULOS ---")
t1.mostrar()
t2.mostrar()

print("\n--- REDONDOS ---")
r1.mostrar()
r2.mostrar()

# COMPARAR CUADRADO Y TRIANGULO
print("\n--- MAYOR AREA ENTRE CUADRADO Y TRIANGULO ---")

area_c = c1.obtenerArea()
area_t = t1.obtenerArea()

if area_c > area_t:
    print("El mayor es el CUADRADO de color:", c1.color)
else:
    print("El mayor es el TRIANGULO de color:", t1.color)
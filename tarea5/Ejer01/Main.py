#main.py
from Libro import Libro
from Biblioteca import Biblioteca


print ("Creando Libros...")
libro1 = Libro("El Quijote", "Miguel de Cervantes", 1605)
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967)
libro3 = Libro("La Sombra del Viento", "Carlos Ruiz Zafón", 2001)
libro4 = Libro("Don Juan Tenorio", "José Zorrilla", 1844)   
print("\nCreando Bibliotecas...")
biblioteca1 = Biblioteca("Biblioteca Central")
biblioteca2 = Biblioteca("Biblioteca Municipal")
print("\nAgregando libros a las bibliotecas...")
biblioteca1.agregarLibro(libro1)    
biblioteca1.agregarLibro(libro2)
biblioteca2.agregarLibro(libro3)
biblioteca2.agregarLibro(libro4)


print("\nVerificando si el libro 'Cien Años de Soledad' está en la Biblioteca Central...")
print ("\n")
biblioteca1.buscarLibro("Cien Años de Soledad")
print("\nVerificando si el libro 'La Sombra del Viento' está en la Biblioteca Central...")
print ("\n")   
biblioteca1.buscarLibro("La Sombra del Viento")


print("\n--- Comparación de Bibliotecas ---")
cant1 = biblioteca1.getCantidad()
cant2 = biblioteca2.getCantidad()

if cant1 > cant2:
    print(f"La biblioteca con más libros es: {biblioteca1}")
elif cant2 > cant1:
    print(f"La biblioteca con más libros es: {biblioteca2}")
else:
    print("Hay un empate:")
    print(biblioteca1)
    print(biblioteca2)

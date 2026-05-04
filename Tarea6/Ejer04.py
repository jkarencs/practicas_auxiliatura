#Por : Karen Jeanette Carrillo Salinas
#Ejercicio 4: 

class Mueble:
    def __init__(self, tipo: str, material: str):
        self.tipo = tipo
        self.material = material

    def __str__(self):
        return f"Mueble(tipo={self.tipo}, material={self.material})"


class Habitacion:
    def __init__(self, nombre: str, tamano: float):
        self.nombre = nombre
        self.tamano = tamano
        self.muebles: list[Mueble] = []  # Lista dinámica en lugar de array fijo

    def agregar_mueble(self, mueble: Mueble):
        self.muebles.append(mueble)

    def cantidad_muebles(self) -> int:
        return len(self.muebles)

    def __str__(self):
        return f"Habitacion(nombre={self.nombre}, tamano={self.tamano}, muebles={self.cantidad_muebles()})"


class Parqueo:
    def __init__(self, capacidad: int, precio_hora: float):
        self.capacidad = capacidad
        self.cant_autos = 0
        self.placas: list[str] = []  # Lista de placas
        self.precio_hora = precio_hora

    def agregar_auto(self, placa: str) -> bool:
        if self.cant_autos < self.capacidad:
            self.placas.append(placa)
            self.cant_autos += 1
            return True
        return False

    def __str__(self):
        return f"Parqueo(capacidad={self.capacidad}, autos={self.cant_autos}, precio_hora={self.precio_hora})"


class Departamento:
    def __init__(self, nro_puerta: int, nro_piso: int):
        self.nro_puerta = nro_puerta
        self.nro_hab = 0
        self.habitaciones: list[Habitacion] = []  # Lista dinámica
        self.nro_piso = nro_piso

    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)
        self.nro_hab = len(self.habitaciones)

    def cantidad_habitaciones(self) -> int:
        return len(self.habitaciones)

    def cantidad_muebles(self) -> int:
        total = 0
        for hab in self.habitaciones:
            total += hab.cantidad_muebles()
        return total

    def agregar_mueble_a_habitacion(self, nombre_hab: str, mueble: Mueble) -> bool:
        for hab in self.habitaciones:
            if hab.nombre == nombre_hab:
                hab.agregar_mueble(mueble)
                return True
        return False

    def __str__(self):
        return f"Departamento(puerta={self.nro_puerta}, piso={self.nro_piso}, habitaciones={self.nro_hab})"


class Edificio:
    def __init__(self, nombre: str, superficie: float):
        self.nombre = nombre
        self.superficie = superficie
        self.cant_deps = 0
        self.departamentos: list[Departamento] = []  # Lista dinámica
        self.parqueo: Parqueo = None

    def agregar_parqueo(self, parqueo: Parqueo):
        self.parqueo = parqueo

    def agregar_departamento(self, departamento: Departamento):
        self.departamentos.append(departamento)
        self.cant_deps = len(self.departamentos)

    def mostrar_departamento_mas_habitaciones_piso(self, piso: int):
        
        #b mostrar.... 
        deps_piso = [d for d in self.departamentos if d.nro_piso == piso]
        if not deps_piso:
            print(f"No hay departamentos en el piso {piso}")
            return
        
        max_hab = max(d.cantidad_habitaciones() for d in deps_piso)
        mejores = [d for d in deps_piso if d.cantidad_habitaciones() == max_hab]
        
        print(f"Departamento(s) con más habitaciones del piso {piso}:")
        for dep in mejores:
            print(f"  - Puerta {dep.nro_puerta}: {dep.cantidad_habitaciones()} habitaciones")

    def agregar_mueble_a_departamento(self, num_puerta: int, piso: int, nombre_hab: str, mueble: Mueble):
        #c Agregar un Mueble al Departamento con num.... 
        for dep in self.departamentos:
            if dep.nro_puerta == num_puerta and dep.nro_piso == piso:
                if dep.agregar_mueble_a_habitacion(nombre_hab, mueble):
                    print(f"Mueble agregado al dep. puerta {num_puerta}, piso {piso}, hab. {nombre_hab}")
                else:
                    print(f"No se encontró la habitación '{nombre_hab}'")
                return
        print(f"No se encontró el departamento puerta {num_puerta} en piso {pismo}")

    def mostrar_departamentos_mas_muebles(self):
        
        #d mostrar al depto con mas m....
        if not self.departamentos:
            print("No hay departamentos")
            return
        
        max_muebles = max(d.cantidad_muebles() for d in self.departamentos)
        mejores = [d for d in self.departamentos if d.cantidad_muebles() == max_muebles]
        
        print(f"Departamento(s) con más muebles ({max_muebles} muebles):")
        for dep in mejores:
            print(f"  - Puerta {dep.nro_puerta}, piso {dep.nro_piso}")

    def mostrar_habitacion_con_mas_muebles_piso(self, piso: int):
        #e. Mostrar el nombre de la habitación con + muebles del pz 
        habitaciones_piso = []
        for dep in self.departamentos:
            if dep.nro_piso == piso:
                for hab in dep.habitaciones:
                    habitaciones_piso.append(hab)
        
        if not habitaciones_piso:
            print(f"No hay habitaciones en el piso {piso}")
            return
        
        max_muebles = max(hab.cantidad_muebles() for hab in habitaciones_piso)
        mejores = [hab for hab in habitaciones_piso if hab.cantidad_muebles() == max_muebles]
        
        print(f"Habitación(es) con más muebles del piso {piso} ({max_muebles} muebles):")
        for hab in mejores:
            print(f"  - {hab.nombre}")

    def es_primo(self, n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def eliminar_departamentos_primos_habitaciones(self):
        #f. Eliminar los deptos  con cant prima de habs
        original_count = len(self.departamentos)
        self.departamentos = [d for d in self.departamentos if not self.es_primo(d.cantidad_habitaciones())]
        eliminados = original_count - len(self.departamentos)
        self.cant_deps = len(self.departamentos)
        print(f"Se eliminaron {eliminados} departamento(s) con cantidad prima de habitaciones")

# run xd 
if __name__ == "__main__":
    # a. Instanciar un objeto Edificio, adicione un Parqueo a dicho edificio.
    edificio = Edificio("Torre Central", 5000.0)
    parqueo = Parqueo(capacidad=50, precio_hora=2.5)
    edificio.agregar_parqueo(parqueo)
    print("a. Edificio creado con parqueo:")
    print(f"   {edificio.nombre}, {edificio.parqueo}\n")

    # Crear deptos
    dep1 = Departamento(nro_puerta=101, nro_piso=1)
    dep2 = Departamento(nro_puerta=102, nro_piso=1)
    dep3 = Departamento(nro_puerta=201, nro_piso=2)
    dep4 = Departamento(nro_puerta=202, nro_piso=2)

    # Crear habs
    hab1 = Habitacion("Sala", 25.0)
    hab2 = Habitacion("Dormitorio", 15.0)
    hab3 = Habitacion("Cocina", 12.0)
    hab4 = Habitacion("Estudio", 10.0)
    hab5 = Habitacion("Sala principal", 30.0)
    hab6 = Habitacion("Dormitorio 1", 18.0)
    hab7 = Habitacion("Dormitorio 2", 16.0)

    # Agregar muebles
    mesa = Mueble("mesa", "madera")
    silla = Mueble("silla", "plástico")
    cama = Mueble("cama", "madera")
    sofa = Mueble("sofá", "tela")
    escritorio = Mueble("escritorio", "metal")

    hab1.agregar_mueble(mesa)
    hab1.agregar_mueble(silla)
    hab2.agregar_mueble(cama)
    hab3.agregar_mueble(mesa)
    hab4.agregar_mueble(escritorio)
    hab4.agregar_mueble(silla)
    hab5.agregar_mueble(sofa)
    hab5.agregar_mueble(mesa)
    hab5.agregar_mueble(silla)
    hab7.agregar_mueble(cama)

    dep1.agregar_habitacion(hab1)
    dep1.agregar_habitacion(hab2)
    dep2.agregar_habitacion(hab3)
    dep2.agregar_habitacion(hab4)
    dep3.agregar_habitacion(hab5)
    dep4.agregar_habitacion(hab6)
    dep4.agregar_habitacion(hab7)

    edificio.agregar_departamento(dep1)
    edificio.agregar_departamento(dep2)
    edificio.agregar_departamento(dep3)
    edificio.agregar_departamento(dep4)

    # b Mostrar al depto que tenga + habss del piso Y (ejm p2)
    print("\nb. Departamento con más habitaciones del piso 2:")
    edificio.mostrar_departamento_mas_habitaciones_piso(2)

    # c Agregar un Mueble al Depto con número de puerta Z del piso X
    print("\nc. Agregando mueble:")
    nuevo_mueble = Mueble("lámpara", "vidrio")
    edificio.agregar_mueble_a_departamento(102, 1, "Estudio", nuevo_mueble)

    #Mostrar al depto que tenga + muebles si hay varios mostrar a todos
    print("\nd. Departamento(s) con más muebles:")
    edificio.mostrar_departamentos_mas_muebles()

    # e Mostrar el nombre de la habitación con más muebles del piso Z
    print("\ne. Habitación con más muebles del piso 2:")
    edificio.mostrar_habitacion_con_mas_muebles_piso(2)

    # f Eliminar los deptos que tengan una cantidad prima de habitaciones
    print("\nf. Eliminando departamentos con cantidad prima de habitaciones:")
    edificio.eliminar_departamentos_primos_habitaciones()
    print(f"   Departamentos restantes: {len(edificio.departamentos)}")
    for dep in edificio.departamentos:
        print(f"   - Puerta {dep.nro_puerta}, habitaciones: {dep.cantidad_habitaciones()}")

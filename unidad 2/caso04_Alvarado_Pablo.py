"""
Nombre:Pablo Alvarado
Curso: M3A
Carrera Desarollo de Sotware

Caso 4: Gasolinera El Arenal
Una gasolinera quiere saber cuántos galones quedan en cada tanque. Programe en Python una clase y un menú de 4 opciones. Tiempo: 1 hora.
La clas
Clase	Atributos	Métodos
Tanque	codigo, combustible, precio, galones	__init__, despachar(cantidad), __str__
despachar(cantidad): si la cantidad es menor o igual a cero, o mayor que galones, muestra un mensaje de error y devuelve False. Si no, resta la cantidad de galones y devuelve True.
Los tanques se guardan en una lista de objetos. El código del nuevo es el tamaño de la lista + 1.
El control de errores con try / except es opcional.
Datos iniciales (dos objetos creados en el programa)
Código	Combustible	Precio por galón	Galones
1	Extra	2.72	500
2	Diesel	1.80	300
Menú
1. Registrar tanque
2. Mostrar tanques
3. Despachar combustible
4. Salir
Pruebas que debe hacer
Opción 1: registre Super / 3.85 / 200 → «Registrado con el código 3.»
Opción 3: código 1, cantidad 50 → «Listo. Quedan 450 galones.»
Opción 3: código 2, cantidad 400 → «Error: solo hay 300 galones.»
Opción 3: código 9 → «Error: no existe ese código.» · Opción 5 → «Opción no válida».
Opción 2: deben verse 3 tanques; el código 1 con 450 galones.
Qué debe entregar
Adjunte su archivo caso04_apellido.py y un PDF con las capturas de las pruebas (o todo en un .zip).

"""

# resolucion del problema
# ejercicio de caso 4


class Tanque:
    def __init__(self, codigo, combustible, precio, galones):
        self.codigo = codigo
        self.combustible = combustible
        self.precio = precio
        self.galones = galones

    def despachar(self, cantidad):
        if cantidad <= 0:
            print("la cantidad debe ser mayor a cero")
            return False
        if cantidad > self.galones:
            print(f"solo hay {self.galones} galones.")
            return False
        self.galones -= cantidad
        print(f"registro exitoso quedan {self.galones} galones.")
        return True

    def __str__(self):
        return f"{self.codigo:<8} {self.combustible:<14} {self.precio:<10.2f} {self.galones:<10}"


tanques = [Tanque(1, "Extra", 2.72, 500), Tanque(2, "Diesel", 1.80, 300)]

while True:
    print("\n--- Gasolinera El Arenal ---")
    print("1. Registrar tanque")
    print("2. Mostrar tanques")
    print("3. Despachar combustible")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        combustible = input("Combustible: ")
        precio = float(input("Precio por galón: "))
        galones = float(input("Galones: "))
        if galones.is_integer():
            galones = int(galones)
        codigo = len(tanques) + 1
        nuevo = Tanque(codigo, combustible, precio, galones)
        tanques.append(nuevo)
        print(f"registrado con el código {codigo} exitosamente")

    elif opcion == "2":
        print(f"{'Código':<8} {'Combustible':<14} {'Precio':<10} {'Galones':<10}")
        for tanque in tanques:
            print(tanque)

    elif opcion == "3":
        codigo_buscar = int(input("Ingrese el código del tanque: "))
        encontrado = None
        for tanque in tanques:
            if tanque.codigo == codigo_buscar:
                encontrado = tanque
                break
        if encontrado is None:
            print("No existe ese código ingrese nuevamente")
        else:
            cantidad = float(input("Cantidad de galones por despachar: "))
            if cantidad.is_integer():
                cantidad = int(cantidad)
            encontrado.despachar(cantidad)

    elif opcion == "4":
        break

    else:
        print("Opción no válida")

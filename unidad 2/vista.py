class VistaTanques:
    def menu(self):
        print("\n--- Gasolinera El Arenal ---")
        print("1. Registrar tanque")
        print("2. Mostrar tanques")
        print("3. Despachar combustible")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        return opcion

    def pedir_datos(self):
        combustible = input("Combustible: ")
        precio = input("Precio por galón: ")
        galones = input("Galones: ")
        return combustible, precio, galones

    def pedir_codigo(self):
        return input("Ingrese el código del tanque: ")

    def pedir_cantidad(self):
        return input("Cantidad de galones por despachar: ")

    def mensaje(self, mensaje):
        print(mensaje)

    def mostrar_tanques(self, tanques):
        print(f"{'Código':<8} {'Combustible':<14} {'Precio':<10} {'Galones':<10}")
        for tanque in tanques:
            print(tanque)

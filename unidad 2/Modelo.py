class Tanque:
    def __init__(self, codigo, combustible, precio, galones):
        self.codigo = codigo
        self.combustible = combustible
        self.precio = precio
        self.galones = galones

    def despachar(self, cantidad):
        if cantidad <= 0 or cantidad > self.galones:
            return False
        self.galones -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo:<8} {self.combustible:<14} {self.precio:<10.2f} {self.galones:<10}"


class ListaTanques:
    def __init__(self):
        self.tanques = []
        self.cargar()

    def cargar(self):
        lista = [Tanque(1, "Extra", 2.72, 500), Tanque(2, "Diesel", 1.80, 300)]
        for t in lista:
            self.tanques.append(t)

    def registrar(self, combustible, precio, galones):
        codigo = len(self.tanques) + 1
        self.tanques.append(Tanque(codigo, combustible, precio, galones))
        return codigo

    def buscar(self, codigo):
        for tanque in self.tanques:
            if tanque.codigo == codigo:
                return tanque
        return None

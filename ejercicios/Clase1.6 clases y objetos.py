#crear una clase
class Libro:
    pass

libro1 = Libro()
print(type(libro1))

#crear el constructor de la clase
class Libro:
    def __init__(self, nombre, autor, estado,lista_libros):
        self.nombre = nombre
        self.autor = autor
        self.estado = estado
        self.lista_libros = lista_libros

    def mostrar(self):
        print("Nombre del libro: ", self.nombre, " Autor: ", self.autor)

    def cambiar_estado(self, estado1):
        self.estado = estado1

    def mostrarlista(self):
        for e in self.lista_libros:

            print(e)

    def __str__(self):
        return f"Nombre del libro: {self.nombre}, Autor: {self.autor}, Estado: {self.estado}, Listas: {self.lista_libros}"

libro2 = Libro("Python intermedio", "Sandoval", "Disponible", [ " Python Basico", "Python intermedio"])
libro2.mostrar()
print(libro2)
libro2.cambiar_estado("prestado")
print(libro2)
libro2.cambiar_estado("Disponible")
print(libro2)
print(libro2.nombre)
libro2.mostrarlista()
print(libro2)
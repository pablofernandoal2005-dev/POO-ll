#Funciones
def suma ():
    print("suma")
suma()

def suma (a, b):
    print(a + b)

suma(3, 2)

def suma (a, b):
    return a + b
resultado = suma(5, 3)
print (resultado)

#decalracion de funciones 
def saludar ():
    print("Hola, mi nombre es Pablo, soy un guia exporador ") 
saludar ()

#funcion con parametros
def calcular_edad (anio_nacimiento, anio_actual):
    print("La edad es : ", anio_actual - anio_nacimiento)
#a = int(input("Ingrese su año de nacimiento: "))
#b = int(input("Ingrese el año actual: "))
#calcular_edad(a, b)

#funciones con retorno 
def calcular_iva(precio, iva):
    return precio * iva
resultado = calcular_iva(10, 0.15)
print("El IVA es : ", resultado)

#funciones con valores por defecto
def calcular_iva(precio, iva = 0.15):
    return precio * iva
resultado = calcular_iva(100)
print("El IVA es : ", resultado)

resultado = calcular_iva(100, 0.14)
print("El IVA es : ", resultado)

#funfiones con lista 
def calcular_par (numeros):
    for e in numeros:
        if e%2==0:
            print ("el numero ", e, " es par")
        else:
            print ("el numero ", e, " es impar")
lista_numeros = range(0,1000,2)
calcular_par (lista_numeros)
lista_numeros = range(5,0,-1)
for e in lista_numeros:
        print (e, end=" ")


#funciones con tuplas
def suma_numeros (*a):
    return sum(a)
print ("la suma es: ", suma_numeros(1, 2, 3))

#funciones con diccionarios

def estudiantes (**lista_estudiantes):
    suma_edades = 0
    for nombre, edad in lista_estudiantes.items():
        print("El estudiante ", nombre, " tiene ", edad, " años")
        suma_edades += edad
    print("La suma de las edades es:", suma_edades)

estudiantes(Steven=24, Kevin=22, Pedro=21, Daniela=20, Maria=20, Gerard=21, David= 19)
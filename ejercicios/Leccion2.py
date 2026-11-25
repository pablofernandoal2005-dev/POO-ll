def ejercicio1():
    print("EJERCICIO 1")
    print("¿Qué imprime el siguiente código?")
    print("")
    print('socio = {"nombre": "Ana", "saldo": 120}')
    print('print(socio.get("correo", "Sin correo"))')
    print("")
    print("")
    print("RESOLUCIÓN:")
    socio = {"nombre": "Ana", "saldo": 120}
    print(socio.get("correo", "Sin correo"))
    print("")
    print("RESPUESTA CORRECTA: d. Sin correo")


def ejercicio2():
    print("EJERCICIO 2")
    print("¿Qué imprime el siguiente código?")
    print("")
    print('texto = "TEC Azuay"')
    print("print(texto[4:7])")
    print("")

    print("")
    print("RESOLUCIÓN:")
    texto = "TEC Azuay"
    print(texto[4:7])
    print("")
    print("RESPUESTA CORRECTA: c. Azu")


def ejercicio3():
    print("EJERCICIO 3")
    print("¿Qué imprime el siguiente código?")
    print("")
    print("a = [1, 2, 3]")
    print("b = a")
    print("b[0] = 5")
    print("print(a)")
    print("")
    print("RESOLUCIÓN:")
    a = [1, 2, 3]
    b = a
    b[0] = 5
    print(a)
    print("")
    print("RESPUESTA CORRECTA: c. [5, 2, 3]")


def ejercicio4():
    print("EJERCICIO 4")
    print("¿Qué imprime el siguiente código?")
    print("")
    print("a = {1, 2, 3, 4}")
    print("b = {3, 4, 5}")
    print("print(len(a & b))")
    print("")

    print("")
    print("RESOLUCIÓN:")
    a = {1, 2, 3, 4}
    b = {3, 4, 5}
    print(len(a & b))
    print("")
    print("RESPUESTA CORRECTA: d. 2")


def ejercicio5():
    print("EJERCICIO 5")
    print("¿Qué imprime el siguiente código?")
    print("")
    print("print(type(10.0))")
    print("")

    print("")
    print("RESOLUCIÓN:")
    print(type(10.0))
    print("")
    print("RESPUESTA CORRECTA: a. <class 'float'>")


def ejercicio6():
    print("EJERCICIO 6")
    print('¿Cuántas veces se imprime "*" en el siguiente código?')
    print("")
    print("for i in range(3):")
    print("    for j in range(2):")
    print('        print("*", end="")')
    print("")

    print("")
    print("RESOLUCIÓN:")
    for i in range(3):
        for j in range(2):
            print("*", end="")
    print("")
    print("")
    print("RESPUESTA CORRECTA: c. 6")


def ejercicio7():
    print("EJERCICIO 7")
    print("¿Qué imprime el siguiente código?")
    print("")
    print("for i in range(3, 0, -1):")
    print('    print(i, end=" ")')
    print("")
    print("")
    print("RESOLUCIÓN:")
    for i in range(3, 0, -1):
        print(i, end=" ")
    print("")
    print("")
    print("RESPUESTA CORRECTA: b. 3 2 1")


def ejercicio8():
    print("EJERCICIO 8")
    print("¿Qué imprime el siguiente código?")
    print("")
    print("for x in [2, 4, 6]:")
    print("    if x == 7:")
    print('        print("Encontrado")')
    print("        break")
    print("else:")
    print('    print("No encontrado")')
    print("")
    print("")
    print("RESOLUCIÓN:")
    for x in [2, 4, 6]:
        if x == 7:
            print("Encontrado")
            break
    else:
        print("No encontrado")
    print("")
    print("RESPUESTA CORRECTA: c. No encontrado")


def ejercicio9():
    print("EJERCICIO 9")
    print("¿Qué imprime el siguiente código?")
    print("")
    print("saldo = 350")
    print("if saldo >= 1000:")
    print('    print("Oro")')
    print("elif saldo >= 100:")
    print('    print("Plata")')
    print("else:")
    print('    print("Básica")')
    print("")
    print("")
    print("RESOLUCIÓN:")
    saldo = 350
    if saldo >= 1000:
        print("Oro")
    elif saldo >= 100:
        print("Plata")
    else:
        print("Básica")
    print("")
    print("RESPUESTA CORRECTA: d. Plata")


def ejercicio10():
    print("EJERCICIO 10")
    print("¿Qué imprime el siguiente código?")
    print("")
    print("print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])")
    print("")
    print("")
    print("RESOLUCIÓN:")
    print([n ** 2 for n in [1, 2, 3, 4] if n % 2 == 0])
    print("")
    print("RESPUESTA CORRECTA: b. [4, 16]")


def ejercicio11():
    print("EJERCICIO 11 - Pares e impares")
    print("Pida números enteros con input() hasta que el usuario escriba fin.")
    print("Guárdelos en una lista y luego, con comprensiones, cree una lista de")
    print("pares y otra de impares. Muestre ambas listas, ordenadas, y la suma de cada una.")
    print("")
    print("RESOLUCIÓN:")
    numeros = []
    while True:
        entrada = input("Ingrese un número (o 'fin'): ")
        if entrada.lower() == "fin":
            break
        numeros.append(int(entrada))

    pares = [n for n in numeros if n % 2 == 0]
    impares = [n for n in numeros if n % 2 != 0]

    print("Los numeros ingresados: ", numeros)
    print("Los pares son: ", sorted(pares), " y la suma es: ", sum(pares))
    print("Los impares son: ", sorted(impares), " y la suma es: ", sum(impares))

def menu_preguntas():
    opcion = ""
    while opcion != "0":
        print("")
        print("===== MENÚ DE PREGUNTAS =====")
        print("1. Pregunta 1: Diccionario con get")
        print("2. Pregunta 2: Slicing de cadenas")
        print("3. Pregunta 3: Listas y referencias")
        print("4. Pregunta 4: Intersección de conjuntos")
        print("5. Pregunta 5: Tipo float")
        print("6. Pregunta 6: Bucles anidados")
        print("7. Pregunta 7: Range descendente")
        print("8. Pregunta 8: For con else")
        print("9. Pregunta 9: if / elif / else")
        print("10. Pregunta 10: Comprensión de listas")
        print("11. Pregunta 11: Pares e impares")
        print("0. Volver al menú principal")
        opcion = input("Elija una pregunta: ")
        print("")
        if opcion == "1":
            ejercicio1()
        elif opcion == "2":
            ejercicio2()
        elif opcion == "3":
            ejercicio3()
        elif opcion == "4":
            ejercicio4()
        elif opcion == "5":
            ejercicio5()
        elif opcion == "6":
            ejercicio6()
        elif opcion == "7":
            ejercicio7()
        elif opcion == "8":
            ejercicio8()
        elif opcion == "9":
            ejercicio9()
        elif opcion == "10":
            ejercicio10()
        elif opcion == "11":
            ejercicio11()
        elif opcion != "0":
            print("Opción no válida")
        if opcion != "0" and opcion in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            input("Presione ENTER para volver al menú...")

nombre = ""
opcion = ""
while opcion != "3":
    print("")
    print("===== MENÚ PRINCIPAL =====")
    print("1. Ingrese nombre")
    print("2. Menú de preguntas")
    print("3. Salir")
    opcion = input("Elija una opción: ")
    if opcion == "1":
        nombre = input("Ingrese su nombre: ")
        print("Bienvenido/a, " + nombre)
    elif opcion == "2":
        if nombre == "":
            print("Primero debe ingresar su nombre (opción 1)")
        else:
            menu_preguntas()
    elif opcion == "3":
        print("Hasta luego " + nombre)
    else:
        print("Opción no válida")
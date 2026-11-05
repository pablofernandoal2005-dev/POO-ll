print(" del 5 ")
for i in range(5):
    print(i)

print(" del 10 ")
for i in range(10):
    print(i)

print(" del 2 al 9 ")
for i in range(2,10):
    print(i)

print(" del 2 al 9 cada 2 numeros ")
for i in range(2,10,2):
    print(i)

print(" del 10 al 0 y -1 ")
for i in range(10,0,-1):
    print(i)

print(" del uno al 100 si es impar o par el numero  ")
for i in range(1,101):
    if i % 2 == 0:
        print(f"{i} es par")
    else:
        print(f"{i} es impar")

#listas
print("foreach")

notas = [6, 8, 9, 10, 3]
for elemento in notas:
    print(elemento)

print("foreach")


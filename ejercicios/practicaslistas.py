notas = [10, 8, 9, 5]
print(notas[1])
notas.append(20)
print(max(notas))
print(notas[1])
notas.append(20)
print(max(notas))
notas.insert(1, 10)
print(len(notas))
print(notas[-1])
print(sum(notas))
print(notas[0:1])   
print(notas[-2])    
print(notas[2])     
print(min(notas))
notas.remove(9)
notas = sorted(notas)
print(notas[2:])
print(notas[:2])



#tuplas 

meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print(meses)

print(meses[0])
print(meses[-1])


estudiante = {
    "nombre": "pablo",
    "cedula": "0107961674",
    "correo": "pablo@example.com",
    "edad": 21,
    "carrera": "Desarrollo de software"
}

print(estudiante.get("nombre"))
print(estudiante.get("cedula"))
print(estudiante.get("correo"))
print(estudiante.get("edad"))
print(estudiante.get("carrera"))
print(estudiante.keys())

conjunto_a = {1,1,5,4,6,8}
conjunto_b = {1,9,6,5,4}

print(conjunto_a & conjunto_b)
print(conjunto_a | conjunto_b)

socio = {
    "cedula": "0102030405",                 # str: puede empezar con 0
    "nombre": "  ana lucía pérez ",          # str con espacios y minúsculas
    "edad": 34,                              # int
    "activo": True,                          # bool
    "garante": None,                         # None: todavía no tiene
    "cuentas": [                             # list de dict
        {"numero": "AH-001", "tipo": "ahorros", "saldo": 1520.75},
        {"numero": "PF-010", "tipo": "plazo fijo", "saldo": 5000.0},
        {"numero": "AH-002", "tipo": "ahorros", "saldo": 80.5},
    ],
}

print(socio.get("nombre").strip())
print(socio.get("nombre").title().strip())
print("la ceduula es", socio.get("cedula"), "la edad es", socio.get("edad"))

print(socio["activo"])

saldos = [cuenta["saldo"] for cuenta in socio["cuentas"]]
print(saldos)


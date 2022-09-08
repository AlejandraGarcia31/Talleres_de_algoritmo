estudiantes = {
    "1": {
           "nombre": "Lorena",
           "nota": 8
    },
    "2": {
        "nombre": "Markel",
           "nota": "4.2"
    },
    "3": {
        "nombre": "Julen",
           "nota": 6.5
    }
}
keys = []
lista = []
lista_estudiantes = 3
while True:
    Datos = (input ("Inserte el nombre y la nota final del estudiante, (La nota debe ser de 0 a 10): "))
    Nombre_Not = (Nombre , Nota) = Datos.split (" ")
    Nombre = str (Nombre)
    Nota  = float (Nota)
    lista.append (Datos)
    lista_estudiantes = lista_estudiantes + 1
    if lista_estudiantes == 11:
        break
    for i in lista:
        estudiantes.update ({f"{lista_estudiantes}" : {"Nombre" : Nombre , "Nota" : Nota}})
print (estudiantes)

lista_notas = []
for i in range (1 , (lista_estudiantes + 1)):
    A = (estudiantes [f"{i}"]["Nota"])
    lista_notas.append (int (A))
Promedio = (sum (lista_notas) / (lista_estudiantes))
print (f"El promedio es de: {Promedio} ")

lista_aprobados = []
lista_perdieron = []
#Aprobaron
for i in range (1 , (lista_estudiantes + 1)):
    if  (estudiantes [f"{i}"] ["Nota"] >= 6.0)
    B = (estudiantes [f"{i}"] ["Nombre"])
    C = (estudiantes [f"{i}"] ["Nota"])
    lista_aprobados.append (B)
    lista_aprobados.append (C)
print (f"Los estudiantes que aprobaron son: {lista_aprobados} ")

#Reprobados
for i in range (1, (lista_estudiantes + 1)):
    if (estudiantes [f"{i}"] ["Nota"] < 6.0):
        D = (estudiantes [f"{i}"]["Nombre"])
        E = (estudiantes [f"{i}"]["Nota"])
        lista_perdieron.append (D)
        lista_perdieron.append (E)
print (f"Los estudiantes que reprobaron son: {lista_perdieron} ")

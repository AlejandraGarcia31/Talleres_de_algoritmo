#Entradas
A = int (input ("Digite el primer numero entero: "))
B = int (input ("digite el segundo numero entero: "))

#Caja negra
while True:
    if (A >= 0):
        A = A-B
        print (A)
    elif (A == 0):
        break
#Entradas
X = int (input ("Aumento de experiencia del mostruo: "))
M = int (input ("Valor de experiencia del mostruo: ")) 

#Caja negra
while (0 < X <= 3):
    if (10 <= M <= (2 ** 32)-1) and ( 0 < X <= 3): 
        Incremento = M * X
        print ( Incremento )
    elif (X == 0 and M == 0):
        break

#Entradas

a = int (input ("Inserte un numero entero que represente a a:") )
b = int (input ("Inserte un numero entero que represente a b:") )
c = int (input ("Inserte un numero entero que represente a c:") )
d = int (input ("Inserte un numero entero que represente a d:") )

#Caja negra

if (d < 1 and d > -1):

#salidas
    print( f"El resultado de la operacion es de: {(a-c)**2}" )
elif (d > 0 ):
    print( f"El resultado de la siguiente operacion es de: {((a-b)**3)/ d}")
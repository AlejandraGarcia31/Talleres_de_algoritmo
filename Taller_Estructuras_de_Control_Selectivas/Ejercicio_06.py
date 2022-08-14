#Entradas

a  = int ( input ( "Inserte el digito que sera A: " ))
b  = int ( input ( "Inserte el digito que sera B: " ))
c  = int ( input ( "Inserte el digito que sera C: " ))
d  = int ( input ( "Inserte el digito que sera D: " ))


# Caja Negra

e =  a , b + 1  # si b < 5 y c >= 5
f =  a , b  # si b y c < 5
g =  a + 1  # Si b y c > 5
n = int ( str ( a ) + str ( b ) + str ( c ) + str ( d ))

# Salidas

print ( f"El numero entero a redondear es el siguiente : { n } " )
if (b<5 and c>=5):
    print ( f"El resultado redondeado sera de : {e}00")
elif (b<5 and c<5) :
    print ( f"El resultado redondeado sera de : {f}00")
else:
    print ( f"El resultado redondeado sera de :  {g} 000")
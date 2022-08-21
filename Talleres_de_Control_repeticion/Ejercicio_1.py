#Entradas
n= int ( input ("Escriba el primer digito entero positivo: "))
k= int ( input ("Escriba el segundo digito entero positivo: "))

#Caja negra
while True: 
    if( k < n ):
        n = n - 1
        print( n )
    elif( n == k ):
     break
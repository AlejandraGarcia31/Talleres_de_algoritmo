#Entradas
Alcohol=1
Diesel=0
Gasolina=2

#Caja negra
while True:
    numero=int(input())
    if numero==1:
        Alcohol=Alcohol+1
    elif numero==2:
        Gasoline=Gasoline+1
    elif numero==3:
        Diesel=Diesel+1
    elif numero==4:
        break
print(f"MUCHAS GRACIAS \nAlcool:{Alcohol} \nGasolina:{Gasolina} \nDiesel:{Diesel}")
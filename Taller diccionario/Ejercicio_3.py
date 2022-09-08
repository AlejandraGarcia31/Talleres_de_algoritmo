usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
                "apellido": "Perurena",
                "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
                "apellido": "Muguruza",
                "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
                "apellido": "Olaizola",
                "password": "123456"
    }
}

Contador = 1
U = str (input ("Inserte su usuario: "))
C = int (input ("Inserte su contraseña: "))
while True:
    if (U == "iperurena" in usuarios and C == 123123):
        A = (usuarios ["iperurena"])
        if (usuarios ["iperurena"] ["password"] == 123123):
            print (A ["nombre"])
            print (A ["apellido"])
        break
    elif (U == "fmuguruza" in usuarios and C == 654321):
        B = (usuarios ["fmuguruza"])
        if (usuarios ["fmuguruza"] ["password"] == 654321):
            print (B ["nombre"])
            print (B ["apellido"])
        break
    elif (U == "aolaizola" in usuarios and C == 123456):
        D = (usuarios ["aolaizola"])
        if (usuarios ["aolaizola"] ["password"] == 123456):
            print (D ["nombre"])
            print (D ["apellido"])
        break
    else:
        U = str (input ("Inserte su usuario: "))
        C = int (input ("Inserte su contraseña: "))
        Contador = Contador + 1
        print ("Usuario o contraseña incorrecto ")
    if Contador == 3:
        break
    
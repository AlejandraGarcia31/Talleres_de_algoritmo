Algoritmo Inicio_numero_invertido
	// entradas
	Escribir "Digite un numero: "
	Leer n
	// caja negra
	Unidad <- n MOD 10
	Decena <- trunc(n/10)
	// salida
	Escribir "Su numero invertido es: " Unidad,Decena
FinAlgoritmo

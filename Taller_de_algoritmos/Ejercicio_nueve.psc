Algoritmo Ejercicio_nueve
	//Entradas
	Escribir "Digite el valor de su salario base: "
	Leer Salario_base
	Escribir "Digite el valor de la primera venta realizada: "
	Leer Venta_uno
	Escribir "Digite el valor de la segunda venta realizada: "
	Leer Venta_dos
	Escribir "Digite el valor de la tercera venta realizada: "
	Leer Venta_tres
	//caja negra
	Comisiones<-((Venta_uno+Venta_dos+Venta_tres)*0.10)
	Salario_final<-(Salario_base+Comisiones)
	//Salidas
	Escribir "El valor de las comisiones es: " Comisiones
	Escribir  "El valor del salario final es: " Salario_final
FinAlgoritmo

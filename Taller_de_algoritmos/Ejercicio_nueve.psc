Algoritmo Ejercicio_nueve
	//Entradas
	Escribir "Digite el valor de su salario base: "
	Leer Salario_base
	Escribir "Digite el valor de las ventas realizadas: "
	Leer Venta_uno
	Leer Venta_dos
	Leer Venta_tres
	//caja negra
	Comisiones<-((Venta_uno*0.10)+(Venta_dos*0.10)+(Venta_tres*0.10))
	Salario_final<-(Salario_base+Comisiones)
	//Salidas
	Escribir "El valor de las comisiones es: " Comisiones
	Escribir  "El valor del salario final es: " Salario_final
FinAlgoritmo

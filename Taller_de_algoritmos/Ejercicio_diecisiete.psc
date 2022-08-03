Algoritmo Ejercicio_diecisiete
	//Entradas
	Escribir "Digite la velocidad en Km/h del vehiculo con mayor velocidad: "
	Leer V1
	Escribir  "Digite la velocidad en Km/h del vehiculo con menor velocidad: "
	Leer V2
	Escribir "Digite la distancia entre ambos vehiculos: "
	//caja negra
	//La distancia del primer vehiculo esta dada por: V1*Tiempo
	//La distancia del segundo vehiculo esta dada por: V2*tiempo+distancia
	//La fornula para hallar el tiempo en el que alcanzara el vehiculo que esta detras al de adelante es: 
	//V1*t=V2*t+d
	//V1-V2*t=distancia
	//V*t=distancia
	//T=d/t
	v1<- (V1)
	v2<- (V2)
	//La fornula para hallar el tiempo en el que alcanzara el vehiculo que esta detras al de adelante es: 
	//V1*t=V2*t+d
	a<- (V1-V2)
	b<- t
	c<- a
	//Tiempo= Distancia/Velocidad
	E<-b/a
	T<- E*60
	//salida
	Escribir "El momento en el que el vehiculo de atras alcanzara al de al frente sera a los " T "minutos "
FinAlgoritmo

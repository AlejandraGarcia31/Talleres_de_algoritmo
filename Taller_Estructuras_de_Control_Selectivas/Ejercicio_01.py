#Entradas

dinero_in= int(input("Digite la cantidad a invertir en el banco "))
interes_banco = float(input("Porcentaje de interes generado al cual paga su banco "))

# Caja Negra

intereses = ( dinero_in * interes_banco / 100 )
if (intereses > 100_000): 
    
#Salidas  
 print ( f"El valor que obtendra al final en su cuenta y que volvera a reinvertir es de: { interes_banco + dinero_in } " , ( f"y el dinero que fue generado por los intereses es de: { intereses } " ))
else:
    print ( f"El valor que obtendra al final en su cuenta sera de: { intereses + dinero_in } y el valor a reinvertir sera de: { dinero_in } " )








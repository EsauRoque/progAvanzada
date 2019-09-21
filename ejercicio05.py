#Ejercicio 5. 
#En muchas jurisdicciones se agrega un pequeño depósito a los envases
#de bebidas para alentar a las personas para reciclarlos En una 
#jurisdicción particular, beba recipientes de un litro o menos tienen
#un depósito de $ 0.10, y los recipientes de bebidas que contienen más
#de un litro tienen depósito de $ 0.25.

#Escriba un programa que lea el número de contenedores de cada tamaño
#del usuario. Su programa debe continuar calculando y mostrando el 
#reembolso que será recibido por devolver esos contenedores. Formatee 
#la salida para que incluya un dólar firmar y siempre muestra 
#exactamente dos decimales.
X=0.25
Y=0.10
print('Bienvenido')
print('Reembolso de importe a botellas')
botella1=int(input('Introduzca la cantidad de botellas menores de un litro:'))
botella2=int(input('Introduzca la cantidad de botellas mayores de un litro:'))
precio1=botella1*X
precio2=botella2*Y
total=precio1+precio2
print('El total a reembolsar es:',total,'dólares')
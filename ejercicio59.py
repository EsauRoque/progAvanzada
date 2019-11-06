#Ejercicio 59. ¿Es válida una matrícula?
#En una jurisdicción particular, las matrículas antiguas consisten en tres 
#letras mayúsculas seguido de tres números. Cuando todas las placas que 
#siguieron ese patrón tenían utilizado, el formato se cambió a cuatro números
#seguidos por tres mayúsculas letras. Escriba un programa que comience 
#leyendo una cadena de caracteres del usuario. Entonces su programa debe 
#mostrar un mensaje que indique si los caracteres son válidos para una placa
#de estilo anterior o una placa de estilo más nueva. Su programa debe mostrar
#un mensaje apropiado si la cadena ingresada por el usuario no es válida para
#Estilo de matrícula.

placa= input('ingrese la placa: ')

tipo_de_placa = ""

if placa[0] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and placa[1] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and placa[2] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ":
	if placa[3] in "0123456789" and placa[4] in "0123456789" and placa[5] in "0123456789":
		tipo_de_placa = "vieja"

elif placa[0] in "0123456789" and placa[1] in "0123456789" and placa[2] in "0123456789" and placa[3] in "0123456789":
	if placa[4] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and placa[5] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ" and placa[6] in "ABCDEFGHIJKLMNOPQRSTUVQRXTUVWXYZ":
		tipo_de_placa = "nueva"
		
if tipo_de_placa == "vieja":
	print("Es una placa vieja.")
elif tipo_de_placa == "nueva":
	print("Es una placa nueva.")
else:
	print("La placa ingresada es erronea.")

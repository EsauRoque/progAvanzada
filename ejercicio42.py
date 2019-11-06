#Ejercicio 42. frecuencia a tener en cuenta
#En la pregunta anterior, convertiste del nombre de la nota a la frecuencia. 
#En esta pregunta escribirás un programa que invierta ese proceso. Comience 
#leyendo una frecuencia del usuario Si la frecuencia está dentro de un Hertz 
#de un valor listado en la tabla en la pregunta anterior, informe el nombre 
#de la nota. De lo contrario, informe que en la frecuencia no corresponde a 
#una nota conocida. En este ejercicio solo necesitas considere las notas 
#enumeradas en la tabla. No hay necesidad de considerar notas de otros
#octavas.
frecuencia=float(input('Introduzca la frecuencia en Hz: '))
nota=' '
if frecuencia>261.63-1 and frecuencia<261.63+1:
	nota="C"
elif frecuencia>293.66-1 and frecuencia<293.66+1:
	nota="D"
elif frecuencia>329.63-1 and frecuencia<329.63+1:
	nota="E"
elif frecuencia>349.23-1 and frecuencia<349.23+1:
	nota="F"
elif frecuencia>392.00-1 and frecuencia<392.00+1:
	nota="G"
elif frecuencia>440.00-1 and frecuencia<440.00+1:
	nota="A"
elif frecuencia>493.88-1 and frecuencia<493.88+1:
	nota="B"
	
if nota==" ":
	print("Esta es una nota erronea.")
else:
	print("Esta es la nota {}.".format(nota))

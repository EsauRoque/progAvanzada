#Ejercicio 26. Tiempo actual.
#Python incluye una biblioteca de funciones para trabajar con el tiempo,
#incluida una función llamado asctime en el módulo de tiempo. Lee la 
#hora actual del reloj interno de la computadora y la devuelve en un 
#formato legible para humanos. Escribir un programa que muestra la hora
#y fecha actuales. Su programa no requerirá ninguna entrada de el 
#usuario.

import time
ahora = time.strftime('%c') 
print ('Fecha y hora ' + time.strftime('%c'))
print ('Fecha '  + time.strftime('%x'))
print ('Hora ' + time.strftime('%X'))
print ('Fecha y hora de la variable %s'  % ahora )
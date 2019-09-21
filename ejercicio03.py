#Ejercicio 3. Area de una habitación.
#escriba un programa que le pregunte al usuario el largo y ancho de una
#habitacion una vez leidos, su programa debe calcular y desplegar el área
#de la habitacion. el largo y ancho debe ser introducido con punto 
#flotante. incluya las unidades (metros) en su mensaje de entrada y 
#salida.

#ejemplo:
#ingresa el largo en metros de la habitacion: 3.3
#ingresa el ancho en metros de la habitacion: 4.8
#el area de la habitacion es de 12.24 metros cuadrados
largo=float(input('Ingrese el largo de la habitacion en metros:'))
ancho=float(input('Ingrese el ancho de la habitacion en metros:'))
print('El area de la habitacion es', largo*ancho,'m^2')

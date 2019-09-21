#ejercicio 4. Area de un campo
#crear un programa que lea el largo y el ancho de un campo de cultivo,
#introducido por el usuario y despliegue el area del campo en acres.

#ejemplo:
#introduce el largo del campo en metros: 10.5
#introduce el ancho del campo en metros: 12.8
#el area del campo es de 0.0331 acres

#1 acre=4046.856 metros cuadrados

largo=float(input('Introduzca el largo del campo en metros:'))
ancho=float(input('Introduzca el largo del campo en metros:'))
area=(largo*ancho)*(1/4046.856)
print('El area es:'+str(area),'acres')
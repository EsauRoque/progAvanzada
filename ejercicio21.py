#Ejercicio 21. Area de un triangulo.
#El área de un triángulo se puede calcular usando la siguiente fórmula,
#donde b es el longitud de la base del triángulo, y h es su altura:
#área = b × h
#      -------
#         2
#Escriba un programa que permita al usuario ingresar valores para b y h. 
#El programa luego debe calcular y mostrar el área de un triángulo con 
#longitud base by altura h.

b=float(input('Introduzca la magnitud de la base:'))
h=float(input('Introduzca la magnitud de la altura:'))
A=(b*h)/2
print('El área del triangulo es:', A)
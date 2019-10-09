#Ejercicio 18. Volumen de un Cilindro
#El volumen de un cilindro se puede calcular multiplicando el área de
#su circular base por su altura. Escriba un programa que lea el radio
#del cilindro, junto con su altura, desde el usuario y calcula su
#volumen. Mostrar el resultado redondeado a un decimal.

import math
r=float(input('Introduzca la magnitud del radio del circulo:'))
h=float(input('Introduzca la altura del cilindro:'))
A=math.pi*(r**2)
V=A*h
print('El volumen del cilindro es:  %.1f'%V)
#Ejercicio 16. Area y volumen
#Escriba un programa que comience leyendo un radio, r, del usuario. El 
#programa continúe calculando y mostrando el área de un círculo con 
#radio r y el volumen de una esfera con radio r. Use la constante pi en
#el módulo matemático en su cálculos.

import math

r=float(input('Introduzca la medida del radio:'))
area=math.pi*(r**2)
print('El area del circulo es:',area)
volumen=(3/4)*math.pi*(r**3)
print('El volumen de la esfera es:',volumen)
#Ejercicio 22. Area de un triangulo(otravez)
#En el ejercicio anterior, creó un programa que calculaba el área de un
#triángulo cuando se conocía la longitud de su base y su altura. También
#es posible calcular el área de un triángulo cuando se conocen las 
#longitudes de los tres lados. Deje s1, s2 y s3 ser la longitud de los
#lados. Sea s = (s1 + s2 + s3) / 2. Entonces el área del triángulo se 
#puede calcular usando la siguiente fórmula:
#área =sqrt(s × (s - s1) × (s - s2) × (s - s3))
#Desarrolle un programa que lea las longitudes de los lados de un 
#triángulo del usuario y muestre su área.

import math

s1=float(input('Introduzca la longitud del lado 1:'))
s2=float(input('Introduzca la longitud del lado 2:'))
s3=float(input('Introduzca la longitud del lado 3:'))
s=(s1+s2+s3)/2
A=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print('El área del triángulo es:',A)
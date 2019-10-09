#Ejercicio 23. Area de un poligono regular.
#Un polígono es regular si sus lados tienen la misma longitud y los
#ángulos entre todos los lados adyacentes son iguales. El área de un 
#polígono regular se puede calcular usando la siguiente fórmula, donde
#s es la longitud de un lado y n es el número de lados: área = n × s^2
#                                                             -------
#                                                        4 × tan (π / n)
#Escriba el programa que lee syn del usuario y luego muestra el área de
#un polígono regular construido a partir de estos valores.

import math
s=float(input('Introduzca la longitud de los lados:'))
n=float(input('Introduzca el número de lados:'))
op1=n*(s**2)
op2=4*math.tan(math.pi/n)
A=op1/op2
print('El area de su poligono regular es:',A)

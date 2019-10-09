#Ejercicio 14. Unidades de altura
#Muchas personas piensan en su altura en pies y pulgadas, incluso en 
#algunos países que utiliza principalmente el sistema métrico. Escriba 
#un programa que lea un número de pies de el usuario, seguido de varias
#pulgadas. Una vez que se leen estos valores, su programa debe calcular
#y mostrar el número equivalente de centímetros.
inches=2.54
ft=12

foot=float(input('Introduzca la cantidad de pies:'))
pulgadas=foot*ft
print(' ',pulgadas,'in')
centimetros=pulgadas*inches
print(' ',centimetros,'cm')
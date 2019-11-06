#Ejercicio 29. Celsius a Fahrenheit y Kelvin.
#Escriba un programa que comience leyendo la temperatura del usuario en 
#grados Celsius. Entonces su programa debe mostrar la temperatura equivalente
#en grados Fahrenheit y grados Kelvin. Los cálculos necesarios para convertir
#entre diferentes unidades de temperatura se pueden encontrar en internet.

Celsius=float(input('Introduzca la temperatura en grados Celsius:'))
Fahrenheit=Celsius*(9/5)+32
Kelvin=Celsius+273.15
print('La temperatura en grados Fahrenheit es:',Fahrenheit)
print('La temperatura en grados Kelvin es:',Kelvin)
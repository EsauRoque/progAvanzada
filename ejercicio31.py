#Ejercicio 31. Suma de los digitos en un entero.
#Desarrolle un programa que lea un número entero de cuatro dígitos del 
#usuario y muestre la suma de los dígitos en el número. Por ejemplo, si el 
#usuario ingresa 3141, entonces su programa debería mostrar 3 + 1 + 4 + 1 = 9.

num=input('Introduzca un número entero:')
suma=0
for cifra in num:
    suma+=int(cifra)
print(suma)
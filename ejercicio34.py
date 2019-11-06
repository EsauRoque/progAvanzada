#Ejercicio 34. Par o impar.
#Escriba un programa que lea un número entero del usuario. Entonces su 
#programa debería mostrar un mensaje que indica si el entero es par o impar.

num=int(input('Introduzca un número entero:'))

if num %2==1:
    print(num,'es impar')
else:
    print(num,'es par')
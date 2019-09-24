#Ejercicio 10. Aritmética.
#Cree un programa que lea los dos valores enteros, a y b, introducidos
#por el usuario.Su programa debe desplegar:

#-La suma de a y b
#-La diferencia cuando a es sutraido de b
#-El producto de a y b
#-El cociente de cuando a divide a b
#-El residuo cuando a divide a b
import math
a=float(input('Ingrese un número:'))
b=float(input('Ingrese un número:'))

suma=a+b
print('La suma de sus números es:',a, '+',b,'=',suma)
resta=b-a
print('La diferencia de sus números es:',b, '-',a,'=',resta)
multiplicacion=a*b
print('El producto de sus números es:',a,'*',b,'=',multiplicacion)
cociente=a/b
print('El cociente de sus números es:',a,'/',b,'=',cociente)
residuo=a%b
print('El residuo del cociente de sus números es:',residuo)
print('El resultado logaritmico de su primer númeor es:',math.log(a, 10))
print('El resultado de su primer número elevado a su segundo número es:',pow(a, b))

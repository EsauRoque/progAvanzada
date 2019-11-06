#Ejercicio 32. Ordenar 3 enteros.
#Cree un programa que lea tres enteros del usuario y los muestre ordenados
#orden (de menor a mayor). Use las funciones min y max para encontrar las más
#pequeñas. y valores más grandes. El valor medio se puede encontrar 
#calculando la suma de los tres valores, y luego restando el valor mínimo y 
#el valor máximo.

a=int(input('Introduzca el primer número:'))
b=int(input('Introduzca el segundo número:'))
c=int(input('Introduzca el tercer número:'))

mn=min(a,b,c)
mx=max(a,b,c)
nd=a+b+c-mn-mx
print('El orden de los números ingresados es:')
print(mn)
print(nd)
print(mx)
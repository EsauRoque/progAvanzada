#Ejercicios 33. Pan del día.
#Una panadería vende hogazas de pan por $ 3.49 cada una. El pan de un día 
#tiene un descuento de 60 por ciento. Escriba un programa que comience 
#leyendo la cantidad de panes de un día pan que se compra al usuario. 
#Entonces su programa debe mostrar el regular precio del pan, el descuento 
#porque tiene un día y el precio total. Todos los valores deben mostrarse 
#con dos decimales y los puntos decimales en todos de los números deben 
#alinearse cuando el usuario ingresa valores razonables.

pan=3.49
descuento=0.60
panes=int(input('Introduzca la cantidad de panes a comprar:'))
precio_regular=panes*pan
con1=descuento*pan
total=precio_regular-con1
print('Precio regular: %5.2f'%precio_regular)
print('Descuento:      %5.2f'%con1)
print('Total:          %5.2f'%total)
#Ejercicio 6. Impuestos y propina.
#hacer un programa en el que el usuario introduzca el nombre de la
#comida que ordeno en un restaurante y su precio. Despues su programa
#debe calcular el subtotal, el iva, y la propina de toda la cuenta. 
#La salida del programa debe parecerse a un ticket de restaurante. 
#Use un iva del 16% y una propina del 15% del subtotal. los valores 
#numericos deben tener dos decimales
iva=0.16
propina=0.15

comida1=(input('Introduzca el nombre de la comida:'))
precio1=float(input('Introduzca el precio de la comida:$'))
comida2=(input('Introduzca el nombre de la comida:'))
precio2=float(input('Introduzca el precio de la comida:$'))
comida3=(input('Introduzca el nombre de la comida:'))
precio3=float(input('Introduzca el precio de la comida:$'))
comida4=(input('Introduzca el nombre de la comida:'))
precio4=float(input('Introduzca el precio de la comida:$'))
comida5=(input('Introduzca el nombre de la comida:'))
precio5=float(input('Introduzca el precio de la comida:$'))
print(comida1,' $',precio1)
print(comida2,' $',precio2)
print(comida3,' $',precio3)
print(comida4,' $',precio4)
print(comida5,' $',precio5)
Subtotal=precio1+precio2+precio3+precio4+precio5
print('Subtotal:$%.2f' %Subtotal)
Subtotal1=(Subtotal*iva)
print('IVA 16%:$%.2f' %Subtotal1)
Subtotal2=(Subtotal*propina)
print('Propina 15%:$%.2f' %Subtotal2)
Total=Subtotal+Subtotal1+Subtotal2
print('Total:$%.2f' %Total)
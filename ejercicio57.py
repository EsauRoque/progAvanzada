#Ejercicio 57. ¿Es un año bisiesto?
#La mayoría de los años tienen 365 días. Sin embargo, el tiempo requerido 
#para que la Tierra orbita alrededor del Sol en realidad es un poco más que
#eso. Como resultado, se incluye un día adicional, el 29 de febrero. En 
#algunos años para corregir esta diferencia. Dichos años se denominan años 
#bisiestos. Las reglas para determinar si un año es o no bisiesto son las 
#siguientes:
#• Cualquier año que es divisible por 400 es un año bisiesto.
#• De los años restantes, cualquier año divisible por 100 no es bisiesto.
#• De los años restantes, cualquier año que sea divisible por 4 es un año 
#bisiesto.
#• Todos los demás años no son bisiestos.
#Escriba un programa que lea un año del usuario y muestre un mensaje que 
#indique si es o no un año bisiesto.

año=int(input('Ingrese el año: '))
año_biciesto=False
if año%400==0:
    año_biciesto=True
elif año%100==0 and not año%400==0:
    año_biciesto=false
elif año%4==0 and not año%100==0 and not año%400==0:
    año_biciesto=True
if año_biciesto:
    print('El año introducido es bisiesto')
else:
    print('El año introducido no es bisiesto')

#Ejercicio 60. Pagos de ruleta
#Una ruleta tiene 38 espacios. De estos espacios, 18 son negros, 18 son rojos
#y dos son verdes. Los espacios verdes están numerados 0 y 00. Los espacios
#rojos están numerados 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 
#32, 34 y 36. Los enteros restantes entre 1 y 36 se usan para numerar los 
#espacios negros. Se pueden hacer muchas apuestas diferentes en la ruleta. 
#Solo consideraremos lo siguiente subconjunto de ellos en este ejercicio:
#• Número único (1 a 36, ​​0 o 00)
#• Rojo contra negro
#• Impar versus par (Tenga en cuenta que 0 y 00 no pagan por par)
#• 1 a 18 versus 19 a 36
#Escriba un programa que simule el giro de una rueda de ruleta utilizando el 
#método aleatorio de Python generador de números Muestra el número 
#seleccionado y todas las apuestas que deben ser pagado Por ejemplo, si se 
#selecciona 13, su programa debería mostrar: El giro resultó en 13 ...
#Pagar 13
#Pagar negro
#Paga impar
#Pague de 1 a 18
#Si la simulación da como resultado 0 o 00, su programa debería mostrar Pagar
#0 o Pague 00 sin más producción.

import random
espacio=random.randint(0, 37)
if espacio==0:
    if random.randint(0, 2)==0:
        print('Paga 00')
    else:
        print('Paga 0')
else:
    print('La ruleta resulto en {}...'.format(espacio))
    print('Paga {}'.format(espacio))
    if espacio==1 or espacio==3 or espacio==5 or espacio==7 or espacio==9 or \
    espacio==12 or espacio==14 or espacio==16 or espacio==18 or espacio==19 \
    or espacio==21 or espacio==23 or espacio==25 or espacio==27 or espacio==30 \
    or espacio==32 or espacio==34 or espacio==36:
        print('Paga rojo')
    else:
        print('Paga negro')
    if espacio>0:
        if espacio%2==0:
            print('Pagan todos')
        else:
            print('Paga impar')
    if espacio>=1 and espacio<=18:
        print('Paga 1 al 18')
    elif espacio>=19 and espacio<36:
        print('Paga 19 al 36')


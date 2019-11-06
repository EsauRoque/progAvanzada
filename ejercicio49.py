#Ejercicio 49. Escala Richter
#La siguiente tabla contiene rangos de magnitud de terremotos en la escala de 
#Richter y sus descriptores:
#Menos de 2.0 Micro
#2.0 a menos de 3.0 Muy menor
#3.0 a menos de 4.0 Menor
#4.0 a menos de 5.0 Light
#5.0 a menos de 6.0 Moderado
#6.0 a menos de 7.0 Fuerte
#7.0 a menos de 8.0 Mayor
#8.0 a menos de 10.0 Genial
#10.0 o más Meteorico
#Escriba un programa que lea una magnitud del usuario y muestre la 
#información apropiada. descriptor como parte de un mensaje significativo. 
#Por ejemplo, si el usuario ingresa 5.5 entonces su programa debe indicar que
#un terremoto de magnitud 5.5 se considera terremoto moderado.

magnitud=float(input('Introduzca la escala del terremoto: '))
escala=' '
if magnitud<2.0:
    escala='Micro'
elif magnitud<3.0 and magnitud>2.0:
    escala='Muy menor'
elif magnitud<4.0 and magnitud>3.0:
    escala='Menor'
elif magnitud<5.0 and magnitud>4.0:
    escala='Light'
elif magnitud<6.0 and magnitud>5.0:
    escala='Moderado'
elif magnitud<7.0 and magnitud>6.0:
    escala='Fuerte'
elif magnitud<8.0 and magnitud>7.0:
    escala='Mayor'
elif magnitud<9.0 and magnitud>8.0:
    escala='Genial'
else:
    escala='Meteorico'
print('La magnitud de la escala ingresada es',escala)

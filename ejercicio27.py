#Ejercicio 27. Índice de masa corporal.
#Escriba un programa que calcule el índice de masa corporal (IMC) de un 
#individuo. Tu programa debe comenzar leyendo una altura y un peso del
#usuario. Luego, debe usar una de las siguientes dos fórmulas para 
#calcular el IMC antes de mostrarlo. Si lees la altura en pulgadas y el
#peso en libras, entonces el índice de masa corporal es calculado usando
#la siguiente fórmula:
#IMC=(peso/(altura ×altura))×703.
#Si lee la altura en metros y el peso en kilogramos, entonces el índice
#de masa corporal se calcula utilizando esta fórmula ligeramente más 
#simple:
#IMC=peso/(altura×altura)

import math
pesolb=float(input('Introduzca su peso en libras:'))
alturainch=float(input('Introduzca su altura en pulgadas:'))
if pesolb>=1 and alturainch>=1:
    IMC=pesolb/(alturainch*alturainch)
    print('IMC=',IMC)
elif pesolb==0 and alturainch==0:
    pesokg=float(input('Introduzca su peso en kiligramos:'))
    alturam=float(input('Introduzca su altura en metros:'))
    IMC1=pesokg/(alturam*alturam)
    print('IMC %.2f'%IMC1)


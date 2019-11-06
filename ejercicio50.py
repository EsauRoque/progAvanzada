#Ejercicio 50. Raíces de una función cuadrática.
#Una función cuadrática univariada tiene la forma f (x) = ax2 + bx + c, donde
#a, b y c son constantes y a no es cero. Se pueden encontrar las raíces de 
#una función cuadrática al calcular los valores de x que satisfacen la 
#ecuación cuadrática ax2 + bx + c = 0. A La función cuadrática puede tener 0,
#1 o 2 raíces reales. Estas raíces se pueden calcular usando la fórmula 
#cuadrática, que se muestra a continuación:
#raíz = −b ± √ b2 - 4ac
#      ----------------          
#             2a
#La parte de la expresión debajo del signo de raíz cuadrada se llama 
#discriminante. Si el discriminante es negativo, entonces la ecuación 
#cuadrática no tiene raíces reales. Si el discriminante es 0, entonces la
#ecuación tiene una raíz real. De lo contrario, la ecuación tiene dos raíces
#reales, y la expresión debe evaluarse dos veces, una vez usando un signo más
#signo, y una vez que usa un signo menos, al calcular el numerador. Escriba 
#un programa que calcule las raíces reales de una función cuadrática. Su 
#programa debe comenzar solicitando al usuario los valores de a, b y c. 
#Entonces debería mostrar un mensaje que indica el número de raíces reales, 
#junto con los valores de las raíces reales (Si alguna).

import math
a=float(input('Introduzca el valor de a: '))
b=float(input('Introduzca el valor de b: '))
c=float(input('Introduzca el valor de c: '))
x1=0
x2=0
raiz=b**2-4*a*c
if raiz<0:
    print('La funcion cuadratrica no tiene valores reales.')
elif raiz==0:
    print('La función tiene un valor real.')
    x=-b/2*a
    print('valor real={}'.format(x))
elif raiz>0:
    print('La función tiene dos valores reales.')
    x1=-b+raiz/2*a
    x2=-b-raiz/2*a
    print('Valores reales={} o {}'.format(x1, x2))
    

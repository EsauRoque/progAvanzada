#Ejercicio 37.Nombra esa forma.
#Escriba un programa que determine el nombre de una forma a partir de su 
#número de lados. Leer el número de lados del usuario y luego informa el 
#nombre apropiado como parte de un mensaje significativo. Su programa debe 
#admitir formas con 3 hasta (e incluyendo) 10 lados. Si se ingresa un número
#de lados fuera de este rango entonces su programa debería mostrar un mensaje
#de error apropiado.

lados=int(input('Introduzca el número de lados de la figura:'))
if lados==3:
    print('La figura es un triangulo.')
elif lados==4:
    print('La figura es un cuadrilatero.')
elif lados==5:
    print('La figura es un pentagono.')
elif lados==6:
    print('La figura es un hexagono.')
elif lados==7:
    print('La figura es un heptagono.')
elif lados==8:
    print('La figura es un octagono.')
elif lados==9:
    print('La figura es un nonecagono.')
elif lados==10:
    print('La figura es un decágono.')
else:
    print('La figura es un poligono.')
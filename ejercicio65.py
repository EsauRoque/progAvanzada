from math import sqrt
perimetro=0

first_x=float(input('Ingrese la coordenada en x: '))
first_y=float(input('Ingrese la coordenada en y: '))

prev_x=first_x
prev_y=first_y

linea=input('Ingrese la parte en x de la coordenada(blanco termina):')
while linea!="":
    x=float(linea)
    y=float(input('Ingrese la parte en y de la coordenadad:'))
    dist=sqrt((prev_x-x)**2+(prev_y-y)**2)
    perimetro=perimetro+dist
    prev_x=x
    prev_y=y
    
    linea=input('Ingrese la parte en x de la coordenadad(blanco termina):')
    
dist=sqrt((first_x-x)**2+(first_y)**2)
perimetro=perimetro+dist

print('El perimetro del poligono es:', perimetro)

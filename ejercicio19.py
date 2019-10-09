#Ejercicio 19. 
import math 

V0=0
g=9.81
d=float(input('Ingrese la distancia en metros:',))
vf=math.sqrt((V0**2)+(2*g*d))
print('La velocidad final es:')
print('Vf= %.2f'% vf,'m/s')

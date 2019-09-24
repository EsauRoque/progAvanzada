#Ejercicio 12. Distancia entre dos puntos de la Tierra.
#La superficie de la tierra es curva y la distancia entre grados de 
#lóngitud varea con la latitud. Como resultado, encontrar la distancia 
#entre dos puntos de la superficie de la tierra es mas complicado que
#usar el teorema de Pitágoras si (t1,g1) y (t2,g2) es la latitud y 
#longitud de dos puntos de la superficie de la tierra. La distancia
#entre esos puntos, a traves de la superficie de la tierra, en kilometros
#es:distancia=6371.01*arcos(sen(t1)*sen(t2)+cos(t1)*cos(t2)*cos(g1-g2))
#Cree un programa que le permita al usuario introducir la latitud y la 
#longitud de dos puntos de la tierra en grados. Su programa debe 
#desplegar la distancia entre esos puntos, en kilometros.Tenga en cuenta
#que las funciones trigonométricas en python trabajan radianes, por lo 
#que debe de convertir el valor introducido por el usuario en grados a 
#radianes antes de utilizar la formula. El módulo math contiene el 
#comando radians, que cambia de grados a radianes.
import math

lat1=float(input('Ingresa la latitud:'))
lat2=float(input('Ingresa la latitud:'))
lon1=float(input('Ingresa la longitud:'))
lon2=float(input('Ingresa la longitud:'))
lat=(math.pi*(lat1))/180
lon=(math.pi*(lon1))/180
lati=(math.pi*(lat2))/180
longi=(math.pi*(lon2))/180
print('latitud en radianes:'+str(lat))
print('latitud en radianes:'+str(lati))
print('longitud en radianes:'+str(lon))
print('longitud en radianes:'+str(longi))
distancia=6371.01*math.acos(math.sin(lat)*math.sin(lati)+math.cos(lat)*math.cos(lati)*math.cos(lon-longi))
print('La distancia entre los puntos es:'+str(distancia))

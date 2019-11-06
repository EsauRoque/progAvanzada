#Ejercicio 28. Escalofrios.
#Cuando el viento sopla en clima frío, el aire se siente aún más frío de lo 
#que realmente es porque el movimiento del aire aumenta la velocidad de 
#enfriamiento de los objetos calientes, como personas. Este efecto se conoce
#como sensación térmica. En 2001, Canadá, el Reino Unido y los Estados Unidos
#adoptaron la siguiente fórmula para calcular el índice de sensación térmica.
#Dentro de la fórmula Ta está el la temperatura del aire en grados Celsius y
#V es la velocidad del viento en kilómetros por hora. 
#WCI = 13.12 + 0.6215Ta − 11.37V**0.16 + 0.3965TaV**0.16. Se puede usar una 
#fórmula similar con diferentes valores constantes con temperaturas en grados
#Fahrenheit y velocidades del viento en millas por hora. Escriba un programa 
#que comience leyendo la temperatura del aire y la velocidad del viento del
#usuario. Una vez que se hayan leído estos valores, su programa debería 
#mostrar la sensación térmica índice redondeado al entero más cercano. 
#El índice de enfriamiento del viento solo se considera válido para 
#temperaturas inferiores o igual a 10 grados centígrados y velocidades del
#viento superiores a 4,8 kilómetros por hora.

comp=13.12
factor1=0.6215
factor2=-11.37
factor3=0.3965
exponente=0.16

temperatura=float(input('Introduzca la temperatura del aire en grados celcius'))
velocidad=float(input('Introduzca la velocidad del viento en kilometros por hora'))
WCI=comp+\
    factor1*temperatura+\
    factor2*velocidad**exponente+\
    factor3*temperatura*velocidad**exponente
print('La sensación termica es:',WCI)
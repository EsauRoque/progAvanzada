#Ejercicio 41. tenga en cuenta la frecuencia
#La siguiente tabla enumera una octava de notas musicales, comenzando con C
#central, a lo largo con sus frecuencias: C4(261.63Hz), D4(293.66Hz), 
#E4(329.63Hz), F4(349.23Hz), G4(392.00Hz), A4(440.00Hz), B4(493.88Hz).
#Comience escribiendo un programa que lea el nombre de una nota del usuario y
#muestra la frecuencia de la nota. Su programa debe admitir todas las notas 
#enumeradas previamente. Una vez que tenga su programa funcionando 
#correctamente para las notas enumeradas anteriormente, debería agregar 
#soporte para todas las notas de C0 a C8. Si bien esto podría hacerse por
#agregando muchos casos adicionales a su declaración if, tal solución es 
#engorrosa, inelegante e inaceptable para los propósitos de este ejercicio. 
#En cambio, deberías explotar la relación entre notas en octavas adyacentes.
#En particular, la frecuencia de cualquier nota en octava n es la mitad de la
#frecuencia de la nota correspondiente en octava n + 1. Al usar esta relación,
#debería poder agregar soporte para las notas adicionales sin agregar casos 
#adicionales a su declaración if. Sugerencia: para completar este ejercicio,
#deberá extraer caracteres individuales del nombre de la nota de dos 
#caracteres para que pueda trabajar con la letra y el número de octava por 
#separado. Una vez que haya separado las partes, calcule frecuencia de la 
#nota en la cuarta octava utilizando los datos de la tabla anterior. Luego 
#divida la frecuencia por 24 − x, donde x es el número de octava ingresado 
#por el usuario. Esto reducirá a la mitad o duplicará la frecuencia la 
#cantidad correcta de veces.

notaenoctava=input('Introduzca la nota musical: ')
nota=notaenoctava[0].upper()
octava=int(notaenoctava[1])
frecuencia=-1
if nota=='C':
    frecuencia=261.63
elif nota=='D':
    frecuencia=293.66
elif nota=='E':
    frecuencia=329.63
elif nota=='F':
    frecuencia=349.23
elif nota=='G':
    frecuencia=392.00
elif nota=='A':
    frecuencia=440.00
elif nota=='B':
    frecuencia=493.88
frecuencia/=2**(4-octava)
print('La frecuencia de la nota es {}Hz'.format(frecuencia))

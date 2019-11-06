#Ejercicio 51. Calificación de letras a puntos de calificación
#En una universidad en particular, las calificaciones con letras se asignan
#a puntos de calificación en la siguiente conducta:
#A+ 4.0
#A  4.0
#A− 3.7
#B+ 3.3
#B  3.0
#B− 2.7
#C+ 2.3
#C  2.0
#C− 1.7
#D+ 1.3
#D  1.0
#F   0
#Escriba un programa que comience leyendo una calificación de letra del 
#usuario. Entonces tu programa debe calcular y mostrar el número 
#equivalente de puntos de calificación. Asegurar que su programa genera un 
#mensaje de error apropiado si el usuario ingresa un mensaje no válido grado 
#de la letra.

calificacion=input('Itroduzca la calificiación en escala de letras: ')
nota=0
if calificacion=='A+' or calificacion=='A':
    nota=4.0
elif calificacion=='A-':
    nota=3.7
elif calificacion=='B+':
    nota=3.3
elif calificacion=='B':
    nota=3.0
elif calificacion=='B-':
    nota=2.7
elif calificacion=='C+':
    nota=2.3
elif calificacion=='C':
    nota=2.0
elif calificacion=='C-':
    nota=1.7
elif calificacion=='D+':
    nota=1.3
elif calificacion=='D':
    nota=1.0
elif calificacion=='F':
    nota=0
else:
    nota='incorrecta.'
print('La calificacion asignada a la nota ingresada es',nota)

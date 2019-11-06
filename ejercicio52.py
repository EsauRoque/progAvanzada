#Ejercicio 52. Calificación de puntos a calificación de letras
#En el ejercicio anterior, creó un programa que convierte una calificación de
#letra en número equivalente de puntos de calificación. En este ejercicio 
#creará un programa que invierte el proceso y convierte de un valor de punto
#de calificación introducido por el usuario a un grado de la letra. Asegúrese
#de que su programa maneje los valores de calificación que se encuentran 
#entre Grados de letras. Estos deben redondearse al grado de letra más 
#cercano. Su programa debe reportar A + para un promedio de calificaciones de
#4.0 (o más).

nota=float(input('Introduzca la calificacion en escala de números: '))
calificacion=' '
if nota>=0 and nota<0.5:
    calificacion='F'
elif nota>=0.5 and nota<1.15:
    calificacion='D'
elif nota>=1.15 and nota<1.5:
    calificacion='D+'
elif nota>1.5 and nota<1.85:
    calificacion='C-'
elif nota>=1.85 and nota<2.15:
    calificacion='C'
elif nota>=2.15 and nota<2.5:
    calificacion='C+'
elif nota>=2.5 and nota<2.85:
    calificacion='B-'
elif nota>=2.85 and nota<3.15:
    calificacion='B'
elif nota>=3.1 and nota<3.5:
    calificacion='B+'
elif nota>=3.5 and nota<3.85:
    calificacion='A-'
elif nota>=3.85 and nota<4.0:
    calificacion='A'
elif nota>=4.0:
    calificacion='A+'
if calificacion!=' ':
    print('La nota mas cercana es {}.'.format(calificacion))
else:
    print('Nota ingresada invalida.')

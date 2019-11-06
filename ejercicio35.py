#Ejercicio 35. años perro.
#Se dice comúnmente que un año humano es equivalente a 7 años de perro. Sin
#embargo esto la conversión simple no reconoce que los perros alcanzan la 
#edad adulta en aproximadamente dos años. Como resultado, algunas personas
#creen que es mejor contar cada uno de los quince años humanos como 10.5 años
#de perro, y luego cuente cada año humano adicional como 4 perros años.
#Escribir un programa que implemente la conversión de años humanos a años de
#perros. descrito en el párrafo anterior. Asegúrese de que su programa 
#funcione correctamente para conversiones de menos de dos años humanos y para
#conversiones de dos o más humanos años. Su programa debe mostrar un mensaje
#de error apropiado si el usuario ingresa Un número negativo.

anios=int(input('Introduzca la edad en años humanos:'))
if anios<=2:
    perros=anios*5.25
    print('La edad en años perro es:',perros)
elif anios<=-1:
    print('La edad ingresada es incorrecta.')
elif anios>=3:
    perros=2*5.25
    perro=perros+(anios-2)*4
    print('La edad en años perro es:',perro)
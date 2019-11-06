#Ejercicio 53. Evaluar empleados
#En una empresa en particular, los empleados son calificados al final de cada
#año. La escala de calificación comienza en 0.0, con valores más altos que
#indican un mejor rendimiento y resultados más grandes plantea. El valor 
#otorgado a un empleado es 0.0, 0.4 o 0.6 o más. Valores entre 0.0 y 0.4, y 
#entre 0.4 y 0.6 nunca se usan. El significado asociado con cada calificación
#se muestra en la siguiente tabla. El monto del aumento de un empleado es 
#$2400.00 multiplicado por su calificación.
#0.0 Unacceptable performance
#0.4 Acceptable performance
#0.6 or more Meritorious performance
#Escriba un programa que lea una calificación del usuario e indique si el
#desempeño fue inaceptable, aceptable o meritorio. El monto  de aumento del 
#empleado también debe ser reportado. Su programa debe mostrar un error 
#apropiado mensaje si se ingresa una calificación no válida.

valor=float(input('Ingrese el valor de incremento del empleado: '))
aumento=' '
if valor==0.0:
    aumento='aumento inaceptable'
elif valor==0.4:
    aumento='aumento aceptable'
elif valor==0.6:
    aumento='amerita aumento'
if aumento!=' ':
    print('De acuerdo con la escala, el empleado tiene "{}".'.format(aumento))
else:
    print('Valor ingresado invalido. (Los valores aceptados son: 0.0, 0.4, 0.6)')
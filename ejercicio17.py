#Ejercicio 17. Capacidad calorifica
#La cantidad de energía requerida para aumentar la temperatura de un
#gramo de material en un grado Celsius es la capacidad calorífica 
#específica del material, C. La cantidad total de energía requerida 
#para elevar m gramos de un material en ΔT grados Celsius puede ser
#calculado usando la fórmula: q = mCΔT. Escriba un programa que lea
#la masa de un poco de agua y el cambio de temperatura. del usuario 
#Su programa debe mostrar la cantidad total de energía que debe ser
#agregado o eliminado para lograr el cambio de temperatura deseado.
#Sugerencia: La capacidad calorífica específica del agua es 4.186 J
#g◦C. Debido a que el agua tiene una densidad de 1.0 gramos por 
#mililitro, puede usar gramos y mililitros indistintamente en este 
#ejercicio Extienda su programa para que también calcule el costo de 
#calentar el agua. La electricidad normalmente se factura utilizando 
#unidades de kilovatios hora en lugar de julios. En esto ejercicio, 
#debe suponer que la electricidad cuesta 8,9 centavos por kilovatio-hora.
#Utilizar su programa para calcular el costo de hervir agua por una 
#taza de café. Sugerencia: deberá buscar el factor para convertir entre 
#julios y kilovatios hora para completar la última parte de este 
#ejercicio.

C=4.186
kwh=2.77*10**-7
electricidad=0.89
T1=float(input('Introduzca la cantidad de grados Celsius inicial:  °C'))
T2=float(input('Introduzca la cantidad de grados Celsius Final:   °C'))
m=float(input('Introduzca la cantidad de masa del agua:'))
q=m*C*(T1-T2)
print('La energia necesaria para el cambio de temperatura es: q=',q)
con=q*kwh
print('La cantidad de Kilowatts hora necesaria es:',con)
pago=con*electricidad
print('El costo para hacer el cambio de temperatura es:',pago)

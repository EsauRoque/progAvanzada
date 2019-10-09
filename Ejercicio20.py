#Ejercicio 20. Ley de gas ideal
#La ley de los gases ideales es una aproximación matemática del 
#comportamiento de los gases como cambio de presión, volumen y 
#temperatura. Por lo general, se indica como: PV = nRT donde P es la
#presión en Pascales, V es el volumen en litros, n es la cantidad de 
#sustancia en moles, R es la constante de gas ideal, igual a 8.314 
#J / molK, y T es la temperatura en grados Kelvin. Escriba un programa
#que calcule la cantidad de gas en moles cuando el usuario suministra la
#presión, el volumen y la temperatura. Pruebe su programa determinando
#la cantidad de moles de gas en un tanque de buceo. Un tanque típico de
#contiene 12 litros de gas a una presión de 20,000,000 Pascales
#(aproximadamente 3,000 PSI). La temperatura ambiente es de 
#aproximadamente 20 grados Celsius o 68 grados Fahrenheit
#Sugerencia: una temperatura se convierte de Celsius a Kelvin al 
#agregarle 273.15. Para convertir una temperatura de Fahrenheit a Kelvin,
#deduzca 32 de ella, multiplíquela por 5/9 y luego agregue 273.15.

R=8.314
K=273.15
P=float(input('Introduzca la presión:'))
V=float(input('Introduzca el volumen:'))
T=float(input('Introduzca la temperatura:'))
n=(P*V)/(R*T)
print('El número de moles es:n=',n)
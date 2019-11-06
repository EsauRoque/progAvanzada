#Ejercicio 30. Unidades de presión.
#En este ejercicio creará un programa que lea la presión del usuario en
#kilopascales. Una vez que se ha leído la presión, su programa debe informar
#el equivalente presión en libras por pulgada cuadrada, milímetros de 
#mercurio y atmósferas. Utilice sus habilidades de investigación para 
#determinar los factores de conversión entre estas unidades.

KPa=float(input('Introduzca la presión en kilopascales:'))
Lb=KPa*0.145
print('La presión en Libras sobre pulgada cuadrada es:',Lb)
mmHg=KPa*7.501
print('La presión en milimetros de mercurio es:',mmHg)
atm=KPa*0.01
print('La presión en atmósferas es:',atm)

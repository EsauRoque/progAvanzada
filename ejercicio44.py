#Ejercicio 44. fecha al nombre de vacaciones
#Canadá tiene tres feriados nacionales que caen en las mismas fechas cada 
#año. Dia de año nuevo Enero 1
#Día de Canadá Julio 1
#Día de Navidad Diciembre 25
#Escriba un programa que lea un mes y un día del usuario. Si el mes y el dia
#coinciden con uno de los días festivos enumerados anteriormente, entonces 
#su programa debería mostrar nombre de vacaciones De lo contrario, su 
#programa debe indicar que el mes ingresado y día no corresponde a un feriado
#de quince días. Canadá tiene dos feriados nacionales adicionales, el Viernes
#Santo y el Día del Trabajo, cuyas fechas varían de año en año. También hay 
#numerosos provinciales y vacaciones territoriales, algunas de las cuales 
#tienen quince fechas, y algunas de las cuales tienen Fechas variables. No 
#consideraremos ninguno de estos días festivos adicionales en este ejercicio.

dia=float(input('Introduzca el día:'))
mes=input('Introduzca el mes:')
if mes=='Enero' and dia==1:
    print('El día Festivo es de Año Nuevo')
elif mes=='Julio' and dia==1:
    print('El día Festivo es de El día de Canadá')
elif mes=='Diciembre' and dia==25:
    print('El día Festivo es de Navidad')
else:
    print('El mes y día que ingreso no coincide con un día festivo o son erroneos')
#Ejercicio 24. Unidades de tiempo.
#Cree un programa que lea una duración del usuario como un número de 
#días, horas, minutos y segundos. Calcule y muestre el número total de 
#segundos representados por esta duración.
SEGUNDOS_POR_MINUTO=60
SEGUNDOS_POR_HORA=3600
SEGUNDOS_POR_DIA=86400
SEGUNDOS=1
Dias=int(input('Introduzca la duración en días:'))
Horas=int(input('Introduzca la duracion en horas:'))
Minutos=int(input('Introduzca la duración en minutos:'))
Segundos=int(input('Introduzca la duración en segundos:'))

Con1=Dias*SEGUNDOS_POR_DIA
Con2=Minutos*SEGUNDOS_POR_MINUTO
Con3=Horas*SEGUNDOS_POR_HORA
Total=Con1+Con2+Con3+Segundos
print('D:',int(Total),'segundos')
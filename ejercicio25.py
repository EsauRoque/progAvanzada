#Ejercicio 25.Unidades de tiempo 2.
#En este ejercicio usted revertirá el proceso descrito en el ejercicio
#previo. Desarrolle un programa que comienze por leer una cantidad de 
#segundos introducidos por el usario. Su programa debe desplegar la 
#cantidad equivalente en la forma de D:hh:mm:SS, don de D son los dias,
#HH las horas y SS son los segundos. Las horas, minutos y segundos deben
#de estar en formato de 2 dígitos como 0 al inicio, si es necesario.
#2dias 2 horas 2 minutos 2 segundos
SEGUNDOS_POR_MINUTO=60
SEGUNDOS_POR_HORA=3600
SEGUNDOS_POR_DIA=86400
SEGUNDOS=1
Segundos=int(input('Introduzca la duración en segundos:'))

Con1=Segundos/SEGUNDOS_POR_DIA
Segundos1=Segundos%SEGUNDOS_POR_DIA
Con2=Segundos1/SEGUNDOS_POR_HORA
Segundos2=Segundos1%SEGUNDOS_POR_HORA
Con3=Segundos2/SEGUNDOS_POR_MINUTO
Segundos3=Segundos2%SEGUNDOS_POR_MINUTO
print('La duración es:',\
       '%d:%02d:%02d:%02d'%(Con1,Con3,Con2,Segundos3))
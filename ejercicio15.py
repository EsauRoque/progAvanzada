#Ejercicio 15. Unidades de distancia
#En este ejercicio, creará un programa que comienza leyendo una medida
#en pies del usuario. Entonces su programa debe mostrar la distancia
#equivalente en pulgadas, yardas y millas. Use Internet para buscar los 
#factores de conversión necesarios si no los tienes memorizados.

inch=12
yd=0.333333
mi=0.000189394

ft=float(input('Introduzca la cantidad de pies:'))
con1=ft*inch
print('La medida en pulgadas es:',con1)
con2=ft*yd
print('La medida en yardas es:',con2)
con3=ft*mi
print('La medida en milla es:',con3)
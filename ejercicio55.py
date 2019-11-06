#Ejercicio 55. frecuencia para nombrar
#La radiación electromagnética se puede clasificar en una de las 7 categorías
#según su frecuencia, como se muestra en la tabla a continuación:
#Ondas de radio Menos de 3 × 10**9
#Microondas 3 × 10**9 a menos de 3 × 10**12
#Luz infrarroja 3 × 10**12 a menos de 4.3 × 10**14
#Luz visible 4.3 × 10**14 a menos de 7.5 × 10**14
#Luz ultravioleta 7.5 × 10**14 a menos de 3 × 10**17
#Rayos X 3 × 10**17 a menos de 3 × 10**19
#Rayos gamma 3 × 10**19 o más
#Escriba un programa que lea la frecuencia de la radiación del usuario y 
#muestre el nombre apropiado.

frecuencia=float(input('Introduzca la frecuencia de radiación: '))
potencia=int(input('Introduzca la potencia de la radiación: '))
if frecuencia<=3.0 and potencia<=9:
    nombre='ondas de radio'
elif frecuencia>3.0 and potencia<=14 or potencia>12:
    nombre='Microondas'
elif frecuencia<=4.3 or frecuencia>3.0 and potencia<=14 or potencia>12:
    nombre='luz infrarroja'
elif frecuencia<=7.5 or frecuencia>4.3 and potencia<=14:
    nombre='luz visible'
elif frecuencia<=7.5 or frecuencia>3.0 and potencia<=17 or potencia>14:
    nombre='luz ultravioleta'
elif frecuencia<=3.0 and potencia<=19 or potencia>17:
    nombre='rayos x'
elif frecuencia<=3.0 and potencia>=19:
    nombre='rayos gamma'
print('La radiación de acuerdo a la frecuencia ingresada es',nombre)
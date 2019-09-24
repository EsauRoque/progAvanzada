#Ejercicio 11. Eficiencia de combustible.
#En los Estados Unidos, la eficiencia del combustible para vehículos
#normalmente se expresa en millas por galón (MPG). En Canadá, la
#eficiencia del combustible normalmente se expresa en litros por cien 
#kilómetros (L / 100 km). Usa tus habilidades de investigación para 
#determinar cómo convertir de MPG a L / 100 km. Luego cree un programa 
#que lea un valor del usuario en América unidades y muestra la eficiencia
#de combustible equivalente en unidades canadienses.

#1mpg=235.21 l/100km

americana=float(input('Introduzca la cantidad de combustible en America (MPG):'))
canadiense=235.21
conversion=americana/canadiense
print('La cantidad de combustible en Canadá es:',conversion,'L/100km')

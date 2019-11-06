#Ejercicio 38. Nombre del mes a la cantidad de días
#La duración de un mes varía de 28 a 31 días. En este ejercicio crearás
#Un programa que lea el nombre de un mes del usuario como una cadena. 
#Entonces tu programa debe mostrar la cantidad de días en ese mes. Mostrar
#"28 o 29 días" para febrero para que se aborden los años bisiestos.

mes=input('Introduzca el mes:')
if mes=='enero' or 'marzo' or 'mayo' or 'julio' or 'agosto' or 'octubre' or\
    'diciembre':
    print('Este mes tiene 31 días')
elif mes=='abril' or 'junio' or 'septiembre' or 'noviembre':
    print('Este mes tiene 30 días')
elif mes=='febrero':
    print('Tiene 28 o 29 días')
else:
    print('El mes que introdijo es invalido')
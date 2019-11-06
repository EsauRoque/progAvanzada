#Ejercicio 43. Caras en dinero
#Es común que aparezcan en su dinero imágenes de los líderes anteriores de un
#país, u otras personas de importancia histórica. Las personas que aparecen 
#en los billetes en los Estados Unidos se enumeran en la siguiente tabla
#Escriba un programa que comience leyendo la denominación de un billete del
#usuario. Luego, su programa debe mostrar el nombre de la persona que aparece
#en el George Washington $1
#Thomas Jefferson $2
#Abraham Lincoln $5
#Alexander Hamilton $10
#Andrew Jackson $20
#Ulysses S. Grant $50
#Benjamin Franklin $100
#billete de la cantidad ingresada. Se debe mostrar un mensaje de error 
#apropiado si no existe tal nota. Si bien los billetes de dos dólares rara 
#vez se ven en circulación en los Estados Unidos, son de curso legal que 
#pueden gastarse como cualquier otra denominación. los Estados Unidos también
#ha emitido billetes en denominaciones de $ 500, $ 1,000, $ 5,000 y $ 10,000 
#para uso público. Sin embargo, los billetes de alta denominación no se han 
#impreso desde 1945 y se descontinuaron oficialmente en 1969. Como resultado,
#no los consideraremos en este ejercicio.

dinero=int(input('Introduzca la denominación del billete: '))
nombre=' '
if dinero==1:
    nombre='George Washington'
elif dinero==2:
    nombre='Thomas Jefferson'
elif dinero==5:
    nombre='Abraham Lincoln'
elif dinero==10:
    nombre='Alexander Hamilton'
elif dinero==20:
    nombre='Andrew Jackson'
elif dinero==50:
    nombre='Ulysses S. Grant'
elif dinero==100:
    nombre='Benjamin Franklin'
if nombre==' ':
   print('El billete no existe.')
else:
    print('El personaje en el billete de $',dinero, 'es', nombre)
 

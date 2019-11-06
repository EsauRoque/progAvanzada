#Ejercicio 40. nombre de un triangulo.
#Un triángulo puede clasificarse en función de la longitud de sus lados como
#isósceles equiláteros o escaleno. Los 3 lados de un triángulo equilátero 
#tienen la misma longitud. Un isósceles el triángulo tiene dos lados que 
#tienen la misma longitud y un tercer lado que es diferente longitud. Si 
#todos los lados tienen diferentes longitudes, entonces el triángulo es 
#escaleno. Escriba un programa que lea las longitudes de 3 lados de un 
#triángulo del usuario. Muestra un mensaje que indica el tipo de triángulo.

lado1=float(input('Introduzca la longitud del lado 1:'))
lado2=float(input('Introduzca la longitud del lado 2:'))
lado3=float(input('Introduzca la longitud del lado 3:'))

if lado1==lado2 and lado2==lado3:
    name='equilatero'
elif lado1==lado2 or lado2==lado3 or lado1==lado3:
    name='isósceles'
else:
    name='escaleno'
print('El triángulo es', name)
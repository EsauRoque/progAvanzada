#Ejercicio 54. Longitudes de onda de luz visible
#La longitud de onda de la luz visible varía de 380 a 750 nanómetros (nm).
#Mientras que la del espectro es continuo, a menudo se divide en 6 colores
#como se muestra a continuación:
#Violeta 380 a menos de 450
#Azul 450 a menos de 495
#Verde 495 a menos de 570
#Amarillo 570 a menos de 590
#Naranja 590 a menos de 620
#Rojo 620 a 750
#Escriba un programa que lea una longitud de onda del usuario e informe su 
#color. Monitor un mensaje de error apropiado si la longitud de onda 
#ingresada por el usuario está fuera de espectro visible.(

longitud=int(input('Introduzca la longitud de onda: '))
espectro=' '

if longitud>=380 and longitud<450:
    espectro='violeta'
elif longitud>=450 and longitud<495:
    espectro='Azul'
elif longitud>=495 and longitud<570:
    espectro='Verde'
elif longitud>=570 and longitud<590:
    espectro='Amarillo'
elif longitud>=590 and longitud<620:
    espectro='Naranja'
elif longitud>=620 and longitud<750:
    espectro='Rojo'
else:
    espectro='incorrecto'
print('El espectro de la longitud de onda que introdujo es',espectro)

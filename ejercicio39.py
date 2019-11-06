#Ejercicio 39. Niveles de sonido.
#La siguiente tabla enumera el nivel de sonido en decibelios para varios 
#ruidos comunes: martillo neumatico (130dB), Cortacésped a gas (106dB), 
#alarma de reloj (70dB), cuarto callado (40dB).
#Escriba un programa que lea un nivel de sonido en decibelios del usuario. 
#Si el usuario ingresa un nivel de decibelios que coincide con uno de los 
#ruidos en la tabla y luego su programa debería mostrar un mensaje que 
#contenga solo ese ruido. Si el usuario ingresa un número de decibelios entre
#los ruidos enumerados, entonces su programa debería mostrar un mensaje 
#indicando entre qué ruidos se encuentra el nivel. Asegúrese de que su
#programa también genere salida razonable para un valor más pequeño que el 
#ruido más bajo en la tabla, y para un valor mayor que el ruido más alto en
#la tabla.

dB=int(input('Introduzca la cantidad de decibelios:'))
if dB==130:
    print('Es el nivel de un martillo neumático')
elif dB==106:
    print('Es el nivel de un Cortacésped a gas')
elif dB==70:
    print('Es el nivel de una alarma de reloj')
elif dB==40:
    print('Es el nivel de un cuarto callado')
elif dB<130 or dB<106:
    print('Es el nivel entre un martillo neumático y una cortadora de cesped')
elif dB<106 or dB<70:
    print('Es el nivel entre una cortadora de cesped y una alarma de relor')
elif dB<70 or dB<40:
    print('Es el nivel entre una alarma de reloj y un cuarto callado')
else:
    print('El valor no esta dentro del rango')
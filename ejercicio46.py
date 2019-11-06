#Ejercicio 46. Estaciones de mes y día.
#El año se divide en cuatro estaciones: primavera, verano, otoño e invierno.
#Mientras que las fechas exactas en que cambian las estaciones varían un poco
#de un año a otro debido a la de la manera en que se construye el calendario,
#utilizaremos las siguientes fechas para este ejercicio:
#Primavera 20 de marzo
#Verano 21 de junio
#Otoño 22 de septiembre
#Invierno 21 de diciembre
#Cree un programa que lea un mes y un día del usuario. El usuario ingresará
#el nombre del mes como una cadena, seguido del día dentro del mes como un
#entero. Luego, su programa debe mostrar la temporada asociada con la fecha 
#en que fue ingresado.

dia=int(input('Introduzca el día: '))
mes=input('Introduzca el mes: ' )
estacion=' '
primavera=False
verano=False
otoño=False
invierno=False

if mes=='marzo' or mes=='abril' or mes=='mayo' or mes=='junio':
    if mes=='marzo' and dia>=20:
        primavera=True
    elif mes=='abril' or mes=='mayo':
        primavera=True
    elif mes=='junio' and dia<21:
        primavera=True

if mes=='junio' or mes=='julio' or mes=='agosto' or mes=='septiembre':
    if mes=='junio' and dia>=21:
        verano=True
    elif mes=='julio' or mes=='agosto':
        verano=True
    elif mes=='septiembre' and dia<22:
        verano=True

if mes=='septiembre' or mes=='octubre' or mes=='noviembre' or mes=='diciembre':
    if mes=='septiembre' and dia>=22:
        otoño=True
    elif mes=='octubre' or mes=='noviembre':
        otoño=True
    elif mes=='diciembre' and dia<21:
        otoño=True

if mes=='diciembre' or mes=='enero' or mes=='febrero' or mes=='marzo':
    if mes=='diciembre' and dia>=20:
        invierno=True
    elif mes=='enero' or mes=='febrero':
        invierno=True
    elif mes=='marzo' and dia<20:
        invierno=True

if primavera:
    print('La fecha ingresada es de primavera.')
elif verano:
    print('La fecha ingresada es de verano.')
elif otoño:
    print('La fecha ingresada es de otoño.')
elif invierno:
    print('La fecha ingresada es de invierno.')

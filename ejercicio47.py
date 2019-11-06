#Ejercicio 47.Dia de cumpleaños y signo astrológico.
#Los horóscopos comúnmente reportados en los periódicos usan la posición del
#sol en el momento del nacimiento para intentar predecir el futuro. Este 
#sistema de astrología divide el año en doce signos del zodiaco, como se
#describe en la tabla a continuación:
#Zodiac sign Date range
#Capricorn December 22 to January 19
#Aquarius January 20 to February 18
#Pisces February 19 to March 20
#Aries March 21 to April 19
#Taurus April 20 to May 20
#Gemini May 21 to June 20
#Cancer June 21 to July 22
#Leo July 23 to August 22
#Virgo August 23 to September 22
#Libra September 23 to October 22
#Scorpio October 23 to November 21
#Sagittarius November 22 to December 21
#Escriba un programa que le pida al usuario que ingrese su mes y día de 
#nacimiento. Entonces su programa debe informar el signo del zodiaco del 
#usuario como parte de una salida adecuada mensaje.

dia=int(input('Introduzca su día de nacimiento:'))
mes=input('Introduzca su mes de nacimiento:')
if dia==22 and mes=='diciembre' and dia<=19 and mes=='enero':
    print('Tu signo astrológico es capricornio')
elif dia==20 and mes=='enero' and dia<=18 and mes=='febrero':
    print('Tu signo astrológico es acuario')
elif dia==19 and mes=='febrero' and dia<=20 and mes=='marzo':
    print('Tu signo astrológico es picis')
elif dia==21 and mes=='marzo' and dia<=19 and mes=='abril':
    print('Tu signo astrológico es aries')
elif dia==20 and mes=='abril' and dia<=20 and mes=='mayo':
    print('Tu signo astrológico es tauro')
elif dia==21 and mes=='mayoo' and dia<=20 and mes=='junio':
    print('Tu signo astrológico es geminis')
elif dia==21 and mes=='junio' and dia<=22 and mes=='julio':
    print('Tu signo astrológico es cancer')
elif dia==23 and mes=='julio' and dia<=22 and mes=='agosto':
    print('Tu signo astrológico es leo')
elif dia==23 and mes=='agosto' and dia<=22 and mes=='septiembre':
    print('Tu signo astrológico es virgo')
elif dia==23 and mes=='septiembre' and dia<=22 and mes=='octubre':
    print('Tu signo astrológico es libra')
elif dia==23 and mes=='octubre' and dia<=21 and mes=='noviembre':
    print('Tu signo astrológico es escorpion')
elif dia==22 and mes=='noviembre' and dia<=21 and mes=='diciembre':
    print('Tu signo astrológico es sagitario')
elif dia>=32:
    print('La fecha introducida es incorrecta.')








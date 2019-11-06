#Ejercicio 58. Siguiente día
#Escriba un programa que lea una fecha del usuario y calcule su sucesor 
#inmediato. Por ejemplo, si el usuario ingresa valores que representan 
#2013-11-18, entonces su programa debería mostrar un mensaje que indique que
#el día inmediatamente posterior al 2013-11-18 es 2013-11-19. Si el usuario 
#ingresa valores que representan 2013-11-30, entonces el programa debe 
#indicar que al día siguiente es 2013-12-01. Si el usuario ingresa valores 
#que representan 31/12/2013, entonces el programa debe indicar que el día 
#siguiente es 01-01-2014. los la fecha se ingresará en forma numérica con 
#tres declaraciones de entrada separadas; uno para el año, uno para el mes y
#otro para el día. Asegúrese de que su programa funcione correctamente para 
#los años bisiestos.

dia=int(input('Introduzca el día: '))
mes=int(input('Introduzca el mes: '))
año=int(input('Introduzca el año: '))
añosiguiente=año
messiguiente=mes
diasiguiente=dia
if mes!=12:
    diasiguiente=año
else:
    if año!=31:
        añosiguiente=año
    else:
        añosiguiente=año+1
if mes!=9 and mes!=4 and mes!=6 and mes!=6 and mes!=11:
    if dia!=31:
        messiguiente=mes   
        diasiguiente=dia+1
    else:
        if mes!=12:
            messiguiente=mes+1
        diasiguiente=1
else:
    if dia!=30:
        messiguiente=mes
        diasiguiente=dia+1
    else:
        if mes!=12:
            messiguiente=mes+1
        else:
            messiguiente=1
        diasiguiente=1
if mes==2:
    añobisiesto=False
    if año%400==0:
        añobisiesto=True
    elif año%100==0 and not year%400==0:
        añobisiesto=False
    elif año%4==0 and not año%100==0 and not año%400==0:
        añobisiesto=True
    if dia==28:
        if añobisiesto:
            messiguiente=mes
            diasiguiente=dia+1
        else:
            messiguiente=mes+1
            diasiguiente=1
    else:
        messiguiente=mes
        diasiguiente=dia+1
print('El siguiente dia es {}-{}-{}.'.format(diasiguiente,messiguiente,añosiguiente))

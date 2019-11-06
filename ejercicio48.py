#Ejercicio 48. Zodiaco chino.
#El zodiaco chino asigna animales a años en un ciclo de 12 años. Un ciclo de
#12 años es se muestra en la tabla a continuación. El patrón se repite a 
#partir de ahí, con 2012 siendo otro año del dragón, y 1999 siendo otro año 
#de la liebre.
#2000 Dragon
#2001 serpiente
#2002 caballo
#2003 Ovejas
#2004 Mono
#2005 Gallo
#2006 perro
#2007 cerdo
#2008 Rata
#2009 Buey
#2010 tigre
#2011 Liebre
#Escriba un programa que lea un año del usuario y muestre el animal asociado
#con ese año Su programa debería funcionar correctamente durante cualquier
#año mayor o igual a cero, no solo los que figuran en la tabla.
año=int(input('Ingrese el año: '))
signo=' '
if año<2000 or año>2011:
    while año<2000:
        año+=12
    while año>2011:
        año-=12

if año==2000:
    signo='Dragon'
elif año==2001:
    signo='serpiente'
elif año==2002:
    signo='caballo'
elif año==2003:
    signo='obeja'
elif año==2004:
    signo='mono'
elif año==2005:
    signo='gallo'
elif año==2006:
    signo='perro'
elif año==2007:
    signo='cerdo'
elif año==2008:
    signo='rata'
elif año==2009:
    signo='buey'
elif año==2010:
    signo='tigre'
elif año==2011:
    signo='liebre'

print('Tu signo zodiacal chino es {}'.format(signo))
print('(según los signos del zodiaco chino, por supuesto ...)')

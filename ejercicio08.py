#Ejercicio 8. Cajas de cereal
#un vendedor de una pagina de abarrotes en linea vende dos tipos de
#cajas de cereal. Cornflakes de 750 gr y trix de 500, cuyo valor debe 
#ser introducido por el usuario. despues, su programa debe calcular y
#mostrar el total del peso (en kilogramos) del envio

caja1=0.750
caja2=0.500
Cornflakes=int(input('Ingrese la cantidad de cajas a enviar de Cornflakes:'))
Trix=int(input('Ingrese la cantidad de cajas a enviar de Trix:'))
Peso1=Cornflakes*caja1
Peso2=Trix*caja2
PesoT=Peso1+Peso2
print('El peso total a enviar es:',PesoT,'kg')
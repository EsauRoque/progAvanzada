#Ejercicio 13. Haciendo el cambio
#Considere el software que se ejecuta en una máquina de autopago. Una
#tarea que debe ser capaz de realizar es determinar cuánto cambio 
#proporcionar cuando el comprador paga para una compra en efectivo.
#Escriba un programa que comience leyendo una cantidad de centavos del 
#usuario como entero. Luego, su programa debe calcular y mostrar las 
#denominaciones de monedas que deberían usarse para dar esa cantidad de 
#cambio al comprador. El cambio debe administrarse utilizando la menor 
#cantidad de monedas posible. Suponga que la máquina está cargada con 
#centavos, monedas de cinco centavos, monedas de diez centavos, monedas
#de veinticinco centavos, loonies y toonies.Una moneda de un dólar se 
#introdujo en Canadá en 1987. Se conoce como Loonie porque un lado de 
#la moneda tiene un loon (un tipo de pájaro). Los dos La moneda de un 
#dólar, conocida como toonie, se introdujo 9 años después. Su nombre es 
#derivado de la combinación del número dos y el nombre del loonie.
#toonie=2 dolares canadiences
#loonie=1 dolar canadience

loonie=100
toonie=200
diez=10
cinco=5
veinti=25

centavos=int(input('Introduzca la cantidad de centavos a cambiar:'))


print(' ',centavos//toonie,'toonies')
centavos=centavos%toonie
print(' ',centavos//loonie,'loonies')
centavos=centavos%loonie
print(' ',centavos//veinti,'cuartos')
centavos=centavos%veinti
print(' ',centavos//diez,'decimos')
centavos=centavos%diez
print(' ',centavos//cinco,'quintos')
centavos=centavos%cinco
print(' ',centavos,'centavos')
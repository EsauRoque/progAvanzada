#Ejercicio 45. ¿De que color es ese cuadro?
#Las posiciones en un tablero de ajedrez se identifican con una letra y un 
#número. La letra identifica la columna, mientras que el número identifica la
#fila.Escriba un programa que lea una posición del usuario. Use una 
#declaración if para determinar si la columna comienza con un cuadrado negro
#o un cuadrado blanco. Luego use modular aritmética para informar el color 
#del cuadrado en esa fila. Por ejemplo, si el usuario ingresa a1 entonces su
#programa debe informar que el cuadrado es negro. Si el usuario ingresa d5
#entonces su programa debe informar que el cuadrado es blanco. Su programa 
#puede asumir que siempre se ingresará una posición válida. No necesita 
#realizar ningún error comprobación.

posicion=input('Ingrese la posición:')
letra=posicion[0].lower()
numero=int(posicion[1])
if letra in 'aceg':
    letraStartsWithBlack=True
else:
    letraStartsWhithBlack=False
if letraStartsWithBlack:
    if numero%2==0:
        blanco=True
    else:
        blanco=False
else:
    if numero%2==0:
        blanco=False
    else:
        blanco=True
if blanco:
    print('El color de la casilla es blanca')
else:
    print('El color de la casilla es negra')

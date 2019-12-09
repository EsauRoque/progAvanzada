# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 15:17:31 2019

@author: stitch
"""

#ejersicio70 
#Uno de los primero ejemplos de encriptacion fue usado por julio cesar. julio cesar necesitaba el enviar 
#instrucciones escritas a sus generales, pero el no queria que sus enemigos  cocnocieran de sus planes 
#en caso de que el mensajefuese interceptado. Coo resultado, el desarrollo lo que despues seria conocido 
#como el cifrado de cesar. La idea destras de este cfrado es simple (y como resultado no tiene proteccion
#contra las tecnicas modernas de hackeo). Cada letra en el mensaje original se mueve tres lugares. Como
#resultado a se convierte en d, b se convierte en e, c se convierte en f, d se convierte en g, etc.
#las ultimas tres letras en el alfabeto se mueven al inicio, es decir, x se convierte en a, y se convierte 
# en b y z se convirte en c.
#Escriba un programa que implemente el cifrado cesar. Permita que el usuario inserte el mensaje y la canidad
#de espacios a moverse, y despues despliegue el mensaje movido. Su programa debe de soportar letras 
#mayusculas y minusculas. su programa tambien debe soportar movimientos con valores negativos de tal manera 
#que los mensajes se puedan cifrar y decifrar.

mensaje=input('ingresa el mensaje: ')
cambio=int(input('introduzca el valor del cambio: '))
nvmen=""
for ch in mensaje:
    if ch>="a" and ch<="z":
      pos=ord(ch)-ord('a')
      pos=(pos+cambio)%26
      newcara=chr(pos+ord('a'))
      nvmen=nvmen+newcara
    elif ch>='A' and ch <='Z':
      pos=ord(ch)-ord('A')
      pos=(pos+cambio)%26
      newcara=chr(pos+ord('A'))
      nvmen=nvmen+newcara
    else:
      nvmen=nvmen+ch
    
print('El mensaje cambiado es: ', nvmen)
    

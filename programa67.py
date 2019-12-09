# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:35:51 2019

@author: stitch
"""

precio_bebe=0.00
precio_niño=14.00
precio_adulto=23.00
precio_señor=18.00

limite_bebe=2
limite_niño=12
limite_adulto=64

total=0

linea=input("Ingrese la edad del huesped (blanco termina):")

while linea != "":
    edad=int(linea)
    
    if edad<=limite_bebe:
        total=total+precio_bebe
    elif edad<=limite_niño:
        total=total+precio_niño
    elif edad<=limite_adulto:
        total=total+precio_adulto
    else:
        total=total+precio_señor
    linea=input("Ingrese la edad del huesped (blanco termina):")
    
print("El total para ese grupo es de $%.2f"%total)
        
        
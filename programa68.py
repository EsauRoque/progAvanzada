# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 00:59:49 2019

@author: stitch
"""

linea=input("Ingresa 8 bits:")
while linea !="":
    if linea.count("0")+linea.count("1") !=8 or len(linea)!=8:
        print("No fueron 8 bits, intentalo de nuevo")
    else:
        unos=linea.count("1")
        if unos%2==0:
            print("El bit de paridad debe ser 0")
        else:
            print("El bit de paridad debe ser 1")
            
    linea=input("Ingresa 8 bits:")
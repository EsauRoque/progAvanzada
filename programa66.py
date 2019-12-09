# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 23:56:25 2019

@author: stitch
"""
A=4.0
A_MINUS=3.7
B_PLUS=3.3
B=3.0
B_MINUS=2.7
C_PLUS=2.3
C=2.0
C_MINUS=1.7
D_PLUS=1.3
D=1.0
F=0
invalido=-1

letra1=input('Ingresa la calificacion en letra: ')
letra1=letra1.upper()
letra2=input('Ingresa la calificacion en letra: ')
letra2=letra2.upper()
letra3=input('Ingresa la calificacion en letra: ')
letr3a=letra3.upper()
while letra1!="" or letra2!="" or letra3!="":
    if letra1=="A+" or letra1=="A" or letra2=="A+" or letra2=="A" or letra3=="A+" or letra3=="A":
        gp=A
    elif letra1=="A-" or letra2=="A-" or letra3=="A-":
        gp= A_MINUS
    elif letra1=="B+"  or letra2=="B+" or letra3=="B+":
        gp =B_PLUS
    elif letra1=="B "  or letra2=="B" or letra3=="B":
        gp =B
    elif  letra1=="B-"  or letra2=="B-" or letra3=="B-":
        gp=B_MINUS
    elif letra1=="C"  or letra2=="C" or letra3=="C":
        gp=C
    elif letra1=="C-"  or letra2=="C-" or letra3=="C-":
        gp =C_MINUS
    elif letra1=="D+"  or letra2=="D+" or letra3=="D+":
        gp = D_PLUS
    elif letra1=="D"  or letra2=="D" or letra3=="D":
        gp=D
    elif letra1=="F"  or letra2=="F" or letra3=="F":
        gp=F
    else:
        gp=invalido
    
    if gp==invalido:
        print("La calificacion no existe")
    else: 
        promedio=((letra1+letra2+letra3)/4.0)*100
        print("El promedio es:", promedio)
        
if letra1=="" or letra2=="" or letra3=="":
    print("fin")
    
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 15:46:30 2019

@author: stitch
"""

n=0
num1=float(input('Ingrese el primer numero: '))
if num1!=0:
   
    while n<=4:
        n=n+1
        num2=float(input('Ingrese el segundo numero: '))
        num3=float(input('Ingrese el tercer numero: '))
        num4=float(input('Ingrese el cuarto numero: '))
        num5=float(input('Ingrese el quinto numero: '))
    if num1==0 or num2==0 or num3==0 or num4==0 or num5==0:
         prom=num1+num2+num3+num4+num5
         print("el promedio de los numeros es: "%prom)
    
        
    else:
        prom=num1+num2+num3+num4+num5
        print("el promedio de los numeros es: "%prom)
if num1==0:
    print=("Error")
        
        
        

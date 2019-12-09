# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 14:50:25 2019

@author: stitch
"""
i=1
j=0
suma=0.0
signo=-1
while i<=30:
    den=(i+1.0)*(i+2.0)*(i+3.0)
    signo=signo*-1
    suma= suma+(signo*4.0/den)
    i=i+2
    pi_aprox=3.0+suma
    j=j+1
    print('Iteracion: ',j, 'pi aprox', pi_aprox)
    

  
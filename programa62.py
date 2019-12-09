# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 15:00:18 2019

@author: stitch
"""

#ejersicio 62. Un suoermercado esta ofreciendo el 60% de descuento en una 
#variedad de productos descontinuados. El supermercado quiere ayudar a sus clientes
# a determinar el precio reducido de su mercancia con una tabla impresa en los aparadores
# donde muestre los precios originales y los precios despues de aplicarse el desc.
#Escriba un programa que use un ciclo while para generar esta tabla mostrando el 
#precio original, l descuento y el nuevo precio para los productos de :
#$4.94, 9.94,14.95, 19.94,24,95. Los descuentos y los nuevos precios deben de ser
#redondeados a dos decimales

precio_original=4.95
print('precio riginal | descuento | precio final')
print('------------------------------------------')
while precio_original<=24.95:
    descuento=precio_original*0.60
    precio_final=precio_original-descuento
   
   
    print("%.2f"% precio_original,('         |'),"%.2f" % descuento,( '             |'), "%.2f"%precio_final)
    precio_original=precio_original+5
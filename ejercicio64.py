penickel=5
nickel=0.05
total=0.00

linea=input("Ingrese el precio del artículo (en blanco para salir):")
while linea!="":
    total=total+float(linea)
    linea=input("Ingrese el precio del artículo (en blanco para salir):")
    linea=input("La cantidad exacta a pagar es de %.02f"%total)
    rounding_indicador=total*100%penickel
if rounding_indicador<penickel/2:
    dintot=total-rounding_indicador/100
else:
    dintot=total+nickel-rounding_indicador/100
    print("el importe en efectivo a pagar es %.02f"%dintot)
    
        

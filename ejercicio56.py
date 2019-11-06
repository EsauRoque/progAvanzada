#Ejercicio 56. Bill de teléfono celular
#Un plan particular de telefonía celular incluye 50 minutos de tiempo al aire
#y 50 mensajes de texto. por $ 15.00 al mes. Cada minuto adicional de tiempo
#en el aire cuesta $ 0.25, mientras que adicional los mensajes de texto 
#cuestan $ 0.15 cada uno. Todas las facturas de teléfonos celulares incluyen
#un cargo adicional de $ 0.44 para respaldar los centros de llamadas al 911,
#y la factura completa (incluido el cargo del 911) es sujeto al 5 por ciento
#de impuesto a las ventas.Escriba un programa que lea la cantidad de minutos
#y mensajes de texto utilizados en un mes del usuario. Muestra el cargo base,
#el cargo por minutos adicionales (si corresponde), cargo adicional por 
#mensaje de texto (si corresponde), la tarifa 911, impuestos y el monto total
#de la factura. Solamente mostrar los cargos adicionales por minutos y 
#mensajes de texto si el usuario incurrió en costos en Estas categorías.
#Asegúrese de que todos los cargos se muestren con 2 decimales.

minutos=int(input('Ingrese la cantidad de minutos utilizados en el mes: '))
mensajes=int(input('Ingrese la cantidad de mensajes utilizados en el mes: '))
cargo_base=15.00
mensaje_adicional=(mensajes-50)*0.15
minuto_adicional=(minutos-50)*0.25
cargo_llamada=0.44
subtotal=cargo_base+mensaje_adicional+minuto_adicional+cargo_llamada
iva=subtotal/100*5
total=subtotal+iva
print()
print('cargo base=$%.2f'%cargo_base)
if minuto_adicional>0:
    print('Cargo por minutos adicionales $%.2f'%minuto_adicional)
elif mensaje_adicional>0:
    print('Cargo por mensajes adicionales $%.2f'%mensaje_adicional)
print('Cargo del centro de llamadas $%.2f'%cargo_llamada)
print('IVA $%.2f'%iva)
print()
print('Total $%.2f'%total)

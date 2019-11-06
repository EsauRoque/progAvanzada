#Ejercicio 36. Vocal o consonante.
#En este ejercicio creará un programa que lee una letra del alfabeto del
#usuario. Si el usuario ingresa a, e, i, o u, entonces su programa debería 
#mostrar un mensaje indicando que la letra ingresada es una vocal. Si el 
#usuario ingresa y entonces su programa debería mostrar un mensaje que 
#indique que a veces y es una vocal, y a veces y es una consonante. De lo 
#contrario, su programa debería mostrar un mensaje que indica que la letra 
#es una consonante.

letra=input('Ingrese una letra del alfabeto:')
if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print('Es una vocal')
elif letra=='y':
    print('Algunas veces es vocal.... Algunas veces es consonante')
else:
    print('Es una consonante')
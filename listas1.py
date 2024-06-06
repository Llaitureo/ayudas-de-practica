"""Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en
una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de
caracteres en un mensaje de salida por pantalla."""

nombres = []
for x in range(3):
    while True:
        nombre = input('ingresa un nombre mayor a 2 letras:')
        if len(nombre)>2 and nombre.isalpha:
            nombres.append(nombre)
            break
        else:
            print('ingrese un nombre sin digitos o simbolos, mayor a 2 letras.')

    nombre_ganador = nombre
    for nombre in nombres:
        if len(nombre)>len(nombres[x]):
            nombre_ganador= nombre
        else:
            pass

print('este es el nombre más largo de los ingresados:',nombre_ganador)
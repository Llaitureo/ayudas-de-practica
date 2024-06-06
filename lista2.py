"""Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para
nombres y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada
los nombres y apellidos."""

nombres = []
apellidos = []

for x in range(3):
    while True:
        nombre = input('ingresa un nombre mayor a 2 letras:')
        if len(nombre)>2 and nombre.isalpha:
            nombres.append(nombre)
            break
        else:
            print('ingrese un nombre sin digitos o simbolos, mayor a 2 letras.')

    while True:
        apellido = input('ingresa un apellido mayor a 2 letras:')
        if len(apellido)>2 and apellido.isalpha:
            apellidos.append(apellido)
            break
        else:
            print('ingrese un apellido sin digitos o simbolos, mayor a 2 letras.')
    

for x, y in zip(nombres, apellidos):
    print(f"nombre:{x}, apellido:{y}")
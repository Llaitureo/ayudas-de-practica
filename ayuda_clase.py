import csv

nombres=[]

for x in range (3):

    while True:
        nombre= input('ingrese un nombre:')
        if len(nombre)>2 and nombre.isalpha():
            print('agregado..')
            nombres.append(nombre)
            break
        else:
            print('letras, mayor a 2 letras.')
    nombre_g = nombre
    for nombre in nombres:
        if len(nombre)>len(nombres[x]):
            nombre_g= nombre
with open ("trabajo.csv","+a") as csvfile:
    escritor= csv.writer(csvfile)
    escritor.writerow(nombres)
print(nombres)
print('este es el nombre mas largo:',nombre_g)
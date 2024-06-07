import csv
import os




matriz=[]

for x in range (3):
    nombres_y_apellidos = []
    nombre = input('ingrese un nombre:')
    apellido= input('ingrese un apellido:')

    nombres_y_apellidos.append(nombre)
    nombres_y_apellidos.append(apellido)
    matriz.append(nombres_y_apellidos)
with open ("trabajo.csv","+a") as csvfile:
    escritor= csv.writer(csvfile)
    escritor.writerow(matriz)
   
os.system('cls')
for x in (matriz):
    print('nombre y apellido:',x)
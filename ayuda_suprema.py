"""un breve tuto de como usar todo :D"""


#librerias

#import json > usalo para el almacenamiento y el intercambio de datos.
"""import json

    #abre el archivo, w es para escribir, +a para escribir sin sobreescribir, ocupa w por ahora.

        open with ("archivo.json","w") as archive:
            json.dump( *aqui va lo que deseas escribir*, archivo)
        #lo que deseas escribir debe ser una variable tipo diccionario, porque json usa clave : valor.

    #abre el archivo, r es para leer.
        
        open with ("archivo.json),"r") as archive:
            lector = json.load(archivo)
            print(lector)
            """

#import os > usalo para importar el sistema operativo de windows.
"""import os
    (lo básico)
    os.system('cls) > usalo para limpiar pantalla.
    time.sleep(*variable*) > usalo para esperar pantalla"""

#import csv > usalo para almacenar datos con estructura excel.
"""import csv
    
    #abre el archivo, w es para escribir, +a para escribir sin sobreescribir, ocupa w por ahora.
    
        open with ("archivo.csv","w") as archive:
            escritor = csv.writer(archive)
            #escoje una de estas opcNúmero.., la que sea mas adecuada.
            opc1.. escritor.writerow( *lista* )
            opc2.. escritor.writerows( *lista de listas (matrizes, tuplas, listas con diccionarios)* )
            opc3.. escritor.writerow("algo", "muy", "importante") > esto escribira por predeterminado en los parentesis.

    #abre el archivo, r es para leer.
        
        open with ("archivo.csv","w") as archive:
            lector = csv.reader(archive)
            for fila in lector:
                print(fila)
            #un bucle para leer todo, la variable fila es lo ya leido, imprimirlo muestra lo que está en el archivo.
            """
#from archivo import > importa datos de un archivo al archivo de trabajo. (ej: funciones a ejercicio)
"""from archivo.algo import * > importa todo lo contenido en el archivo."""




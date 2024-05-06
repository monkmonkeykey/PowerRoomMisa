import json
import numpy as np
import pandas as pd
import os

directorio_json = "D:/DEV/JOSUE/PowerRoomMisa/presidente/json/"  # Asegúrate de que la ruta termina en '/'
directorio_csv = "D:/DEV/JOSUE/PowerRoomMisa/presidente/csv/"  # Asegúrate de que la ruta termina en '/'

text = []
duration = []
start = []

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio_json)

# Imprimir la lista de archivos
for archivo in archivos:
    print(archivo)
    archivo_path = os.path.join(directorio_json, archivo)  # Usa os.path.join para crear la ruta del archivo
    try:
        with open(archivo_path, "r") as j:
            mydata = json.load(j)
            print(mydata)
            
            for item in mydata:
                text.append(item["text"])
                start.append(item["start"])
                duration.append(item["duration"])
                
            df = pd.DataFrame({"text": text, "start": start, "duration": duration})
            csv_path = os.path.join(directorio_csv, archivo[:-5] + '.csv')  # Asegúrate de que eliminas '.json' antes de añadir '.csv'
            df.to_csv(csv_path, index=False)
            text.clear()
            start.clear()
            duration.clear()

    except Exception as e:
        print(f"Error procesando el archivo {archivo}: {e}")  # Imprime el error para facilitar la depuración

import json
import numpy as np
import pandas as pd
import os


directorio_json = "E:/subtitulos/json/"#Directorio de archivos json
directorio_csv = "E:/subtitulos/csv/"#Directorio de archivos csv
"""
directorio_json = "/Volumes/Untitled/subtitulos/json/"#Directorio de archivos json
directorio_csv = "/Volumes/Untitled/subtitulos/csv/"#Directorio de archivos csv
"""
text = []
duration = []
start = []

# Obtener la lista de archivos en el directorio
archivos = os.listdir(directorio_json)

# Imprimir la lista de archivos
for archivo in archivos:
    print(archivo)
    try:
        with open (directorio_json + archivo, "r") as j:
            mydata = json.load(j)
            print ((mydata))
            
            for i in range(len(mydata)):
                text.append(mydata[i]["text"])
                start.append(mydata[i]["start"])
                duration.append(mydata[i]["duration"])
            a = np.array(text)
            b = np.array(start)
            c = np.array(duration)
            df = pd.DataFrame({"text" : a, "start" : b, "duration" : c})
            df.to_csv(directorio_csv +  archivo[:-4] + '.csv', index=False)
            text.clear()
            start.clear()
            duration.clear()

    except Exception as e:
        continue

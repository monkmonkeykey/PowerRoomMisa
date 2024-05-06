# -*- coding: utf-8 -*-
from pytube import Playlist, YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import time
import numpy as np
import pandas as pd
import os
import urllib.parse
import re

s = '='
contador = 0
json_name = []
mp4_name = []

directorio = "jsonsss"  # Directorio para guardado de subtitulos
if not os.path.exists(directorio):  # Crea el directorio si no existe
    os.makedirs(directorio)

links_lista = []
prefijo_youtube = 'https://www.youtube.com/watch?v='

def obtener_lista(url):
    try:
        links_lista = Playlist(url)
        links = Playlist(url)
        print(links_lista)
        if links:
            for link in links_lista:
                try:
                    posicion = link.find(s) + 1
                    url_actual = link[posicion:]
                    video_actual = YouTube(prefijo_youtube + url_actual)
                    transcripcion = YouTubeTranscriptApi.get_transcript(video_actual.video_id, languages=['es'])
                    formateador = JSONFormatter()
                    json_formateador = formateador.format_transcript(transcripcion)
                    titulo_actual = video_actual.title
                    titulo_actual = re.sub(r'[\\/*?:"<>|]', '_', titulo_actual)  # Evita caracteres ilegales en nombres de archivos
                    nombre_archivo = os.path.join(directorio, f'{titulo_actual} [{video_actual.video_id}].json')
                    print("Descargando: " + nombre_archivo)
                    with open(nombre_archivo, 'w', encoding='utf-8') as archivo_json:
                        archivo_json.write(json_formateador)
                        print("Se ha descargado correctamente: " + nombre_archivo)
                except Exception as e:
                    print(e)
                    continue
        else:
            print("Error")
    except Exception as e:
        raise Exception("Error al obtener la lista de reproducción")

# Llamada de ejemplo a la función
obtener_lista("https://www.youtube.com/watch?v=X4CnXGYFV7o&list=PL-wEE8VmWaJ3BoPk-jxOrjOp711iP_Oqg&ab_channel=GobiernodeM%C3%A9xico")

# Instrucciones de Instalación y Uso

Este README proporciona instrucciones detalladas para instalar dependencias y ejecutar los siguientes scripts de Python:

1. Script para extraer transcripciones.
2. Script para eliminar archivos corruptos y descargar videos de YouTube utilizando yt-dlp.
3. Script para convertir archivos JSON de transcripciones de YouTube a archivos CSV.

## 1. Instalación de Python

Si aún no tienes Python instalado en tu sistema, puedes descargarlo e instalarlo desde [python.org](https://www.python.org/downloads/).

## 2. Instalación de Dependencias

### Dependencias Comunes:

```
pip install pytube youtube-transcript-api numpy pandas
```

### Dependencias Adicionales para el Script 2:

#### Instalación de yt-dlp (solo para Windows):

1. Descarga el archivo ejecutable de `yt-dlp` desde [GitHub](https://github.com/yt-dlp/yt-dlp/releases).
2. Coloca el ejecutable `yt-dlp.exe` en una ubicación accesible desde la línea de comandos.
3. Agrega la ubicación del ejecutable `yt-dlp.exe` al PATH del sistema.

### Dependencias Adicionales para el Script 3:

No se requieren dependencias adicionales, ya que el script utiliza bibliotecas estándar de Python (`json` y `os`).

## 3. Ejecutar los Scripts

### Script 1: Extracción de transcripciones

Ejecuta el siguiente comando en tu terminal o símbolo del sistema:

```
python descarga_subtitulos_Win.py
```

### Script 2: Eliminar Archivos Corruptos y Descargar Videos de YouTube

Asegúrate de haber instalado yt-dlp siguiendo las instrucciones proporcionadas anteriormente. Luego, ejecuta el siguiente comando:

```
python descarga_mananeras.py
```


### Script 3: Convertir Archivos JSON a CSV

Ejecuta el siguiente comando para convertir archivos JSON a CSV:

```
python conversor_json_a_csv.py
```


---

Si tienes alguna pregunta o encuentras algún problema durante la instalación o ejecución de los scripts, no dudes en preguntar.

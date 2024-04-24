import os

def descarga(youtube_url):
    try:
        archivos = []
        directorio =  'F:\PowerRoom\media\mananera'
        contenido = os.listdir(directorio)
        
        for file in contenido:
            if os.path.isfile(os.path.join(directorio, file)) and file.endswith('.part'):
                archivos.append(file)
        
        totalFileserrores = len(archivos)
        print("Número de archivos a eliminar:", totalFileserrores)

        for aBorrar in archivos:
            os.remove(os.path.join(directorio, aBorrar))

        print('Se han eliminado los archivos corruptos')

        os.chdir(directorio)
        print('Nos encontramos en el directorio', os.getcwd())

        if os.getcwd() == directorio:
            command = f'yt-dlp.exe -f 18 "{youtube_url}"'
            os.system(command)
            print('Se ha completado la descarga')
        else:
            print('Directorio INCORRECTO')
            print('REVISAR QUE EL DISCO DURO ESTÉ BIEN CONECTADO')
            print(directorio)

    except Exception as e:
        print("Ocurrió una excepción:", str(e))

# Ejemplo de uso:
hipervinculo_youtube = 'https://www.youtube.com/playlist?list=PL-wEE8VmWaJ3BoPk-jxOrjOp711iP_Oqg'
descarga(hipervinculo_youtube)
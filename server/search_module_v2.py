import csv
from pathlib import Path
directorio = '/Volumes/PowerRoom/csv'
#directorio = './csv'
def search(query, directory=directorio, filename_pattern='*.csv'):
    """Busca un término en archivos CSV y devuelve los resultados."""
    results = []
    path = Path(directory).resolve()
    print("Buscando en el directorio:", path)

    # Verificar si el directorio existe y es accesible
    if not path.is_dir():
        return {"status": "Error", "message": "El directorio no existe o no es accesible"}

    try:
        for csv_file in path.glob(filename_pattern):
            try:
                with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        if 'text' in row and query.lower() in row['text'].lower():
                            results.append({
                                "file": csv_file.name,
                                "text": row['text'],
                                "start": row['start'],
                                "duration": row['duration']
                            })
            except UnicodeDecodeError:
                print(f"No se pudo leer el archivo {csv_file} con UTF-8. Intentando con ISO-8859-1...")
                try:
                    with open(csv_file, mode='r', newline='', encoding='iso-8859-1') as file:
                        reader = csv.DictReader(file)
                        for row in reader:
                            if 'text' in row and query.lower() in row['text'].lower():
                                results.append({
                                    "file": csv_file.name,
                                    "text": row['text'],
                                    "start": row['start'],
                                    "duration": row['duration']
                                })
                except Exception as e:
                    print(f"Error al leer el archivo {csv_file} con ISO-8859-1: {e}")
            except Exception as e:
                print(f"Error al procesar el archivo {csv_file}: {e}")
    except Exception as e:
        print(f"Error al buscar en el directorio {directory}: {e}")
        return {"status": "Error", "message": str(e)}

    return {"status": "OK", "results": results}

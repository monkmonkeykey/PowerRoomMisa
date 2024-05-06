import csv
from pathlib import Path
# directorio = 'D:\\DEV\\JOSUE\\PowerRoomMisa\\server\\csv'
directorio = './csv'
def search(query, directory=directorio, filename_pattern='*.csv'):
    """Busca un término en archivos CSV y devuelve los resultados."""
    results = []
    path = Path(directory).resolve()
    print(path)
    for csv_file in path.glob(filename_pattern):
        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if query.lower() in row['text'].lower():  # Se busca en la col 'text'
                    results.append({
                        "file": csv_file.name,
                        "text": row['text'],
                        "start": row['start'],
                        "duration": row['duration']
                    })

    return {"status": "OK", "results": results}

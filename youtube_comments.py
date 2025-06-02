from dotenv import load_dotenv
import os
from googleapiclient.discovery import build
import pandas as pd

# Cargar variables del archivo .env
load_dotenv()

# Leer la clave API desde el .env
api_key = os.getenv('API_KEY')

# ID del video de YouTube del que quieres extraer comentarios
video_id = 'a1Femq4NPxs'  # Pon aquí el ID del video real

# Crear el cliente de YouTube con la clave
youtube = build('youtube', 'v3', developerKey=api_key)

# Preparar la solicitud para obtener los comentarios
request = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    maxResults=100,           # Número máximo de comentarios a traer
    textFormat='plainText'    # Para traer texto sin formato
)

# Ejecutar la solicitud
response = request.execute()

# Lista para guardar los comentarios
comentarios = []

# Extraer los comentarios del resultado
for item in response['items']:
    comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
    comentarios.append(comment)

# Crear un DataFrame con pandas para manejar los datos
df = pd.DataFrame({'Comentario': comentarios})

# Guardar los comentarios en un archivo CSV
df.to_csv('comentarios_youtube.csv', index=False, encoding='utf-8-sig')

print(f"Se guardaron {len(comentarios)} comentarios en 'comentarios_youtube.csv'")


# Ejercicios NLP

Este proyecto contiene scripts para extraer comentarios de videos de YouTube y analizarlos usando técnicas de procesamiento de lenguaje natural (NLP).

## Archivos incluidos

- `youtube_comments.py`: Extrae comentarios de un video de YouTube usando la API.
- `analisis_comentarios.py`: Realiza análisis de sentimientos sobre los comentarios.
- `analisis_vader.py`: Usa la librería VADER para análisis básico de sentimientos.
- `comentarios_youtube.csv`: Archivo con comentarios extraídos.

## Requisitos

- Python 3.x
- Librerías: google-api-python-client, pandas, python-dotenv, vaderSentiment

## Uso

1. Configura tu clave API en un archivo `.env` (no subas tu clave a GitHub).
2. Ejecuta `youtube_comments.py` para descargar comentarios.
3. Ejecuta los scripts de análisis para procesar los comentarios.



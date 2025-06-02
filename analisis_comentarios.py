import pandas as pd

# Cargar datos desde el archivo CSV
df = pd.read_csv('comentarios_youtube.csv')

# Mostrar las primeras filas para verificar que se cargaron bien
print("Comentarios cargados:")
print(df.head())

# Contar cuántos comentarios hay
total_comentarios = df.shape[0]
print(f"\nTotal de comentarios: {total_comentarios}")

# Listas simples de palabras clave para clasificar sentimientos
palabras_positivas = ['bueno', 'excelente', 'me gusta', 'perfecto', 'recomiendo', 'feliz', 'genial']
palabras_negativas = ['malo', 'terrible', 'no me gusta', 'pésimo', 'odio', 'triste', 'horrible']

def clasificar_sentimiento(texto):
    texto = texto.lower()
    for palabra in palabras_positivas:
        if palabra in texto:
            return 'Positivo'
    for palabra in palabras_negativas:
        if palabra in texto:
            return 'Negativo'
    return 'Neutral'

# Aplicar la función a la columna Comentario y crear nueva columna Sentimiento
df['Sentimiento'] = df['Comentario'].apply(clasificar_sentimiento)

# Mostrar resultados resumidos
print("\nResumen de sentimientos:")
print(df['Sentimiento'].value_counts())

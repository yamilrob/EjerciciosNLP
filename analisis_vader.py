import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Cargar datos desde el CSV que guardaste
df = pd.read_csv('comentarios_youtube.csv')

analyzer = SentimentIntensityAnalyzer()

# Función para clasificar sentimiento según VADER
def clasificar_sentimiento_vader(texto):
    puntaje = analyzer.polarity_scores(texto)
    compound = puntaje['compound']
    if compound >= 0.05:
        return 'Positivo'
    elif compound <= -0.05:
        return 'Negativo'
    else:
        return 'Neutral'

# Aplicar función a cada comentario y crear nueva columna
df['Sentimiento'] = df['Comentario'].apply(clasificar_sentimiento_vader)

# Mostrar resumen
print("Resumen de sentimientos con VADER:")
print(df['Sentimiento'].value_counts())

# Opcional: mostrar los primeros comentarios con su sentimiento
print("\nPrimeros comentarios analizados:")
print(df[['Comentario', 'Sentimiento']].head())

from typing import List, Tuple
import pandas as pd 
import emoji 

def q2_time(file_path: str) -> List[Tuple[str, int]]:

    #Metodo uusado para extraer los emojis del diccionario generado en la columna content_emoji
    def extraer_emojis(lista_diccionarios):
        emojis = [d.get('emoji', '') for d in lista_diccionarios]
        return emojis

    #Parametros iniciales
    chunksize = 3000
    columnas_lectura = ['content']
    chunks = []

    # Leer el archivo JSON en bloques, al hacer la lectura por bloques o de manera segmentada permite que no se genere un consumo excesivo de memoria,
    # para optimizar tiempo y recursos se puede jugar con el tamaño de lectura del archivo.
    for chunk in pd.read_json(file_path, lines=True,  chunksize=chunksize):
        chunk=chunk[columnas_lectura]  
        chunk['content_emoji'] = chunk['content'].apply(lambda x: emoji.emoji_list(x)) #Función de biblioteca Emoji
        chunk = chunk[chunk['content_emoji'].apply(len) != 0]
        chunks.append(chunk)

    #Concatenación de dataframe
    df = pd.concat(chunks,ignore_index=True)
    df['emojis'] = df['content_emoji'].apply(extraer_emojis)

    #Recorrido en la columna del dataframe para extraer los emojis encontrados 
    lista_emojis = [emoji for sublist in df['emojis'] for emoji in sublist]

    #Conteo de emojis para generar salida
    conteo_emojis = pd.Series(lista_emojis).value_counts().reset_index()
    conteo_emojis.columns = ['Emoji', 'N# Usos']
    conteo_emojis = conteo_emojis.sort_values(by='N# Usos', ascending=False)
    salida_emojis = conteo_emojis.head(10)
    return salida_emojis.values

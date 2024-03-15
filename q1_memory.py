from typing import List, Tuple
from datetime import datetime
import pandas as pd 

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
 
    #Ejercicio N#1 (optimización memoria)
    #Parametros iniciales
    dynamic_key = 'username'
    chunksize = 10000
    columnas_lectura = ['date','user']

    chunks = []
    # Leer el archivo JSON en bloques, al hacer la lectura por bloques o de manera segmentada permite que no se genere un consumo excesivo de memoria,
    # se podria reducir aún más el consumo de memoria reduciendo el tamaño del bloque de lectura pero afectaria  el tiempo de ejecución 
    for chunk in pd.read_json(file_path, lines=True, chunksize=chunksize):
        #Filtrado de columnas 
        chunk=chunk[columnas_lectura]  
        chunk['date'] = pd.to_datetime(chunk['date']).dt.date
        chunk[dynamic_key + '_'] = chunk['user'].apply(lambda x: x.get(dynamic_key))
        chunks.append(chunk)

    #Une el Dataframe
    df = pd.concat(chunks,ignore_index=True)
    #Agrupa las fechas
    agrupacion_fechas = df.groupby(['date']).size().reset_index(name='tweets').sort_values(by='tweets', ascending=False).head(n=10)
    #Agrupa los usuarios
    agrupacion_usuarios = df.groupby(['date','username_']).size().reset_index(name='tweets').sort_values(by='tweets', ascending=False)
    #Genera el dataframe con los usuarios que tienen más tweets por fecha
    usuarios_max_por_fecha = agrupacion_usuarios.loc[agrupacion_usuarios.groupby('date')['tweets'].idxmax()]
    #Unión de dataframes apartir de la columna date como llave 
    salida = pd.merge(agrupacion_fechas['date'], usuarios_max_por_fecha[['date','username_']], on='date',how='left')
    return salida.values
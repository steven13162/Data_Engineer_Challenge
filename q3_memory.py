from typing import List, Tuple
import pandas as pd 
import numpy as np 

def q3_memory(file_path: str) -> List[Tuple[str, int]]:

    #Parametros iniciales
    dynamic_key = 'username'
    chunksize = 10000

    chunks = []

    for chunk in pd.read_json(file_path, lines=True, chunksize=chunksize):
        chunk[dynamic_key + '_'] = chunk['user'].apply(lambda x: x.get(dynamic_key))
        chunk['conteo_menciones'] = chunk['mentionedUsers'].str.len()
        chunk['conteo_menciones'] = np.where(np.isnan(chunk['conteo_menciones']), 0, chunk['conteo_menciones'])

        chunks.append(chunk)

    #Une el Dataframe
    df = pd.concat(chunks,ignore_index=True)
    usuarios_menciones = df.groupby(['username_'])['conteo_menciones'].sum().reset_index(name='#_menciones').sort_values(by='#_menciones', ascending=False).head(n=10)
    return usuarios_menciones.values

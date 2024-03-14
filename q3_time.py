from typing import List, Tuple
import pandas as pd 
import numpy as np

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    dynamic_key = 'username'
    df = pd.read_json(file_path, lines=True)

    #Ejercicio N#3
    df[dynamic_key + '_'] = df['user'].apply(lambda x: x.get(dynamic_key))
    df['conteo_menciones'] = df['mentionedUsers'].str.len()
    df['conteo_menciones'] = np.where(np.isnan(df['conteo_menciones']), 0, df['conteo_menciones'])
    usuarios_menciones = df.groupby(['username_'])['conteo_menciones'].sum().reset_index(name='#_menciones').sort_values(by='#_menciones', ascending=False).head(n=10)
    return usuarios_menciones.values

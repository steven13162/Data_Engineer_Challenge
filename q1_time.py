from typing import List, Tuple
from datetime import datetime
import pandas as pd 

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    #Parametro inicial
    dynamic_key = 'username'

    #La lectura se podria hacer de una manera más eficiente al segmentar el archivo, no obstante se esta buscando un mejor rendimiento. 
    #En mi computador la ejecución tomo 6,78 segundos
    df = pd.read_json(file_path, lines=True)

    #Ejercicio N#1 (optimización tiempo)
    df['date']=pd.to_datetime(df['date']).dt.date
    df[dynamic_key + '_'] = df['user'].apply(lambda x: x.get(dynamic_key))
    #Agrupa las fechas
    agrupacion_fechas = df.groupby(['date']).size().reset_index(name='tweets').sort_values(by='tweets', ascending=False).head(n=10)
    #Agrupa los usuarios
    agrupacion_usuarios = df.groupby(['date','username_']).size().reset_index(name='tweets').sort_values(by='tweets', ascending=False)
    #Genera el dataframe con los usuarios que tienen más tweets por fecha
    usuarios_max_por_fecha = agrupacion_usuarios.loc[agrupacion_usuarios.groupby('date')['tweets'].idxmax()]
    #Une los dataframes  trayendo la info que se requiere para la salida, se hace esto porque se tiene las fechas en un lado, pero hace falta el usuario que más tweets tuvo en las fechas
    #salida = pd.merge(agrupacion_fechas, usuarios_max_por_fecha[['date','username_']], on='date',how='left')
    salida = pd.merge(agrupacion_fechas['date'], usuarios_max_por_fecha[['date','username_']], on='date',how='left')

    return salida.values
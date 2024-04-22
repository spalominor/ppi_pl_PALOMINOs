# Importar librerias necesarias
import pandas as pd
import plotly.express as px


def mapa_calor(df: pd.DataFrame, codigos: str, valores: str):
    """
    Esta función crea un mapa de calor de la población de los Estados Unidos.
    
    Args:
        df (pd.DataFrame): DataFrame con los datos de población.
        codigos (str): Nombre de la columna con los códigos de los estados.
        valores (str): Nombre de la columna con los valores de población.
        
    Return:
        mapa: Objeto de plotly.
    """
    mapa = px.choropleth(df, locations=codigos, locationmode="USA-states",
                         color=valores, scope="usa",
                         color_continuous_scale="Viridis",
                         range_color=(0, max(df[valores])),
                         labels={'poblacion':'Poblacion'}
                        )
    
    return mapa
    
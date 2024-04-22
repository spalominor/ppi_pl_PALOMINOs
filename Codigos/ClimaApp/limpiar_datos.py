# Importar librerias necesarias
import pandas as pd



def mover_punto(geom):
    """
    Mueve el punto decimal de las coordenadas 4 espacios a la izquierda.
    
    Args:
        string: Geometría en formato WKT
        Ejemplo:
            POINT (-37037.90 40416.775)

    Returns:
        string: Geometría con punto decimal movido a la izquierda
        Ejemplo:
            POINT (-37037.90 40416.775)
    """
    longitud, latitud = geom.strip('POINT (').strip(')').split(' ')
    nueva_longitud = float(longitud) * 0.00001
    nueva_latitud = float(latitud) * 0.00001
    return "POINT ({0} {1})".format(nueva_longitud, nueva_latitud)


# Definir distancia de movimiento
distancia_x = -4

# Cargar datos (Archivo de 802536 filas y 6 columnas)
df = pd.read_csv('temp_mensual_espacial_p.csv')

# Eliminar columnas innecesarias
df.drop(columns=['FID', 'id_punto', 'mes', 'agno'], inplace=True)

# Eliminar las filas duplicadas (Archivo de 66878 filas y 2 columnas)
df_limpio = df.drop_duplicates()

# Mover punto decimal a la izquierda
df_limpio['geom'] = df_limpio['geom'].apply(mover_punto)

# Visualizar información de los datos
print(df_limpio.info())

# Convertir los datos a un archivo CSV
df_limpio.to_csv('temperatura.csv', index=False)
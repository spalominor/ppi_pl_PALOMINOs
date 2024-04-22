# Importar librerias necesarias
import pandas as pd
import geopandas as gpd
from shapely import wkt

# Leer el archivo CSV limpio
df = pd.read_csv('temperatura.csv')

# Convertir la columna de geometría de formato WKT a geometrías de Shapely
df['geom'] = df['geom'].apply(wkt.loads)

# Crear un GeoDataFrame
gdf = gpd.GeoDataFrame(df['geom'], geometry='geom')

# Crear un índice espacial
indice_espacial = gdf.sindex

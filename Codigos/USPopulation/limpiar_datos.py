# Importar librerias necesarias
import pandas as pd

# Importar las abreviaciones de cada estado y el orden de las columnas
from utiles import abreviacion, nuevas_columnas



# Cargar el dataset de la poblacion década de los 10's
df_2010 = pd.read_csv('us-population-2010-2019.csv')

# Cargar el dataset de la poblacion década de los 20's
df_2020 = pd.read_csv('us-population-2020-2023.csv')

# Eliminar columnas que no se usaran
df_2020.drop(columns=['state'], inplace=True)

# Unir ambos datasets
df_poblacion_2010_2023 = pd.concat([df_2010, df_2020], axis=1)

# Cambiar el nombre de la columna states a estados
df_poblacion_2010_2023.rename(columns={'states': 'estado'}, inplace=True)

# Crear una columna con la abreviación de cada estado
df_poblacion_2010_2023['abreviacion'] = [
    abreviacion[estado] 
    for estado in df_poblacion_2010_2023['estado']
    ]

# Cambiar el orden de las columnas del dataset
df_poblacion_2010_2023.reindex(columns=nuevas_columnas)

# Guardar el dataset en un archivo CSV
df_poblacion_2010_2023.to_csv('us-population-2010-2023.csv', index=False)

# Cambiar la forma del dataset
df_poblacion = df_poblacion_2010_2023.melt(
    id_vars=['estado', 'abreviacion', 'id'],
    var_name='año',
    value_name='poblacion'
)

# Cambiar el tipo de dato de la columna año
df_poblacion['año'] = df_poblacion['año'].astype(int)

# Eliminar las comas de miles de la columna poblacion
df_poblacion['poblacion'] = df_poblacion['poblacion'].str.replace(',', '')

# Cambiar el tipo de dato de la columna poblacion
df_poblacion['poblacion'] = df_poblacion['poblacion'].astype(int)

# Cambiar el tipo de dato de la columna estado
df_poblacion['estado'] = df_poblacion['estado'].astype(str)

# Guardar el dataset en un archivo CSV
df_poblacion.to_csv('us-population.csv', index=False)

# Imprimir la información del dataset
print(df_poblacion_2010_2023.head())
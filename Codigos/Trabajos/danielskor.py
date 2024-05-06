# Importar librerías necesarias
import pandas as pd



# Cargar el archivo Excel en un DataFrame
df = pd.read_csv("History.csv")

# Convertir la columna de fechas al formato de fecha y hora de Pandas
df['Date'] = pd.to_datetime(df['Date'], format='%Y.%m.%d')

# Ordenar el DataFrame por fecha
#df.sort_values(by='Date', inplace=True)

# Iterar sobre las fechas únicas en el DataFrame
for fecha in df['Date'].unique():
    # Seleccionar la primera fila para esta fecha que no tenga la posición "ALL", si existe
    filas_fecha = df[(df['Date'] == fecha) & (df['Position'] != "ALL")]
    if not filas_fecha.empty:
        primer_row = filas_fecha.iloc[0]
        
        # Obtener el ID de la posición
        id_posicion = primer_row['Position']
        
        # Eliminar todas las filas con este ID en las fechas subsiguientes
        indices_a_eliminar = df[(df['Position'] == id_posicion) & (df['Date'] > fecha)].index
        df.drop(indices_a_eliminar, inplace=True)

# Guardar el DataFrame modificado en un nuevo archivo CSV
df.to_csv("datos_procesados.csv", index=False)

# Cargar el archivo Excel en un DataFrame
df = pd.read_csv("datos_procesados.csv")

# Convertir la columna de fechas al formato de fecha y hora de Pandas
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Convertir la fecha y hora al formato deseado por el cliente (por ejemplo, YYYY.M.D)
df['Date'] = df['Date'].dt.strftime('%Y.%m.%d')

# Guardar el DataFrame en un archivo Excel
df.to_excel("History_cleaned.xlsx", index=False)
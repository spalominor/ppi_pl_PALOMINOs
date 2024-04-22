# Importar librerias necesarias
import streamlit as st
import pandas as pd

# Importar funciones necesarias
from graficas import mapa_calor



def calcular_crecimiento(año):
    """
    Esta función calcula el crecimiento de la población de los Estados Unidos
    en un año específico.
    
    Args:
        año (int): Año para el cual se desea calcular el crecimiento.
        
    Return:
        crecimiento (int): Crecimiento de la población en el año especificado.
    """
    # Filtrar los datos para el año especificado
    df_año = df_poblacion[df_poblacion['año'] == año]
    
    # Filtrar los datos para el año anterior
    df_año_anterior = df_poblacion[df_poblacion['año'] == año-1]
    
    # Calcular el crecimiento de la población en el año por cada estado
    df_crecimiento = df_año[
        "poblacion"].to_numpy() - df_año_anterior["poblacion"].to_numpy()
    
    # Calcular la población total en el año
    poblacion = df_año['poblacion'].sum()
    
    # Calcular la población total en el año anterior
    poblacion_anterior = df_año_anterior['poblacion'].sum()
    
    # Calcular el crecimiento de la población
    crecimiento = poblacion - poblacion_anterior
    
    # Retornar el valor del crecimiento
    return crecimiento, pd.Series(df_crecimiento)


# Cargar datos
df_poblacion = pd.read_csv('us-population.csv')

# Configurar la vista general de la página
st.set_page_config(
    page_title="US Population",
    page_icon="🗽",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Definir las columnas de la página
col1, col2 = st.columns([1, 5])

# Definir la barra lateral
with st.sidebar:
    # Imprimir el titulo de la barra lateral
    st.title("US Population")
    
    # Imprimi el subtitulo de la barra lateral
    st.write("Esta página muestra la población de los Estados Unidos.")
    
    # Definir el menu de seleccion de año
    año = st.selectbox("Selecciona un año", list(range(2023, 2009, -1)))
    
    # Filtrar los datos para el año seleccionado
    df_poblacion_año = df_poblacion[df_poblacion['año'] == año]

# Definir la vista de la columna pequeña
with col1:
    # Imprimir el titulo de la columna pequeña
    st.subheader("Crecimiento")
    
    if int(año) > 2010:
        # Calcular el crecimiento de la población
        crecimiento, df_crecimiento = calcular_crecimiento(año)
        
        # Calcular la población total en ese año
        poblacion = df_poblacion[df_poblacion['año'] == año]['poblacion'].sum()
        
        # Imprimir el crecimiento de la población
        st.success(f"+{crecimiento:,} personas")      
        
        # Imprimir el titulo de la seccion
        st.subheader("Porcentaje de crecimiento")
        
        # Imprimir el porcentaje de crecimiento
        st.success(f"+{(crecimiento/poblacion)*100:.2f}%")
        
        # Imprimir el titulo de la seccion
        st.subheader("Estado con mayor crecimiento")
        
        # Encontrar el estado con mayor crecimiento
        indice_mayor = df_crecimiento.idxmax()
               
        # Buscar el nombre del estado con mayor crecimiento
        estado_mayor_crecimiento = df_poblacion_año.iloc[
            indice_mayor]['estado']
        
        # Imprimir el estado con mayor crecimiento
        st.write(estado_mayor_crecimiento)
        
        # Imprimir el crecimiento del estado con mayor crecimiento
        st.success(f"+{df_crecimiento.max()} personas")
        
        # Imprimir el titulo de la seccion
        st.subheader("Estado con menor crecimiento")
        
        # Encontrar el estado con menor crecimiento
        indice_menor = df_crecimiento.idxmin()
        
        # Buscar el nombre del estado con menor crecimiento
        estado_menor_crecimiento = df_poblacion_año.iloc[
            indice_menor]['estado']
        
        # Imprimir el estado con menor crecimiento
        st.write(estado_menor_crecimiento)
        
        # Imprimir el crecimiento del estado con menor crecimiento
        if df_crecimiento.min() < 0:
            # Si el crecimiento es negativo, poner en rojo
            st.error(f"{df_crecimiento.min()} personas")
        else:
            # Si el crecimiento es positivo, agregar el signo de suma
            st.success(f"+{df_crecimiento.min()} personas")
    elif int(año) == 2010:
        # Si el año es 2010, no hay datos
        st.write("No hay datos para el año 2010")

    
# Definir la vista de la columna grande
with col2:
    # Imprimir el titulo de la columna grande
    st.header("Población de los Estados Unidos")
    
    # Imprimir el subtitulo de la columna grande
    st.write("""Mapa de calor de la población de los Estados Unidos 
             por cada estado.""")
    
    # Mostrar el mapa si hay un ño seleccionado
    if año:
        # Crear el mapa de calor
        mapa = mapa_calor(df_poblacion_año, 'abreviacion', 'poblacion')
        
        # Mostrar el mapa de calor
        st.plotly_chart(mapa, use_container_width=True)
    
    # Imprimir el titulo de la tabla
    st.header("Poblacion por estado")
    
    # Imprimir la tabla con los datos de población
    st.dataframe(df_poblacion_año.sort_values(by='poblacion', ascending=False),
                 hide_index=True,
                 width=1000,
                )   
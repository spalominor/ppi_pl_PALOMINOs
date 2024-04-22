# Importar librerías necesarias
import streamlit as st
import geopandas as gpd
from geopy.geocoders import Nominatim
from indexar import indice_espacial, df



def main():
    """
    Función principal de la aplicación. Define la vista de la aplicación web.
    Esta función se ejecuta al cargar la aplicación web.
    
    Args:
        None

    Returns:
        None
    """
    # Establecer la configuración de la página
    st.set_page_config(
        page_title="ClimaApp 🌤️🌡️",
        page_icon=":partly_sunny:",
        layout="wide"
    )

    # Establecer el título de la aplicación
    st.title("ClimaApp 🌤️🌡️")

    # Crear una barra de búsqueda en la barra lateral
    ubicacion = st.sidebar.text_input("Buscar ubicación")

    # Crear un botón con texto "Prueba con Cancún" y ancho de 200 píxeles
    if st.sidebar.button("Prueba con Cancún"):
        # Asignar "Cancún" a la ubicacion si se hace clic en el botón
        ubicacion = "Cancún"
        
        # Escribir un mensaje indicando que se ha seleccionado Cancún
        st.write("Has seleccionado: Cancún")

    # Crear un botón con texto "Prueba con New York" y ancho de 200 píxeles
    if st.sidebar.button("Prueba con New York"):
        # Asignar "New York" a la ubicacion si se hace clic en el botón
        ubicacion = "New York"
        
        # Escribir un mensaje indicando que se ha seleccionado New York
        st.write("Has seleccionado: New York")

    # Crear un botón con texto "Prueba con Alaska" y ancho de 200 píxeles
    if st.sidebar.button("Prueba con Alaska"):
        # Asignar "Alaska" a la ubicacion si se hace clic en el botón
        ubicacion = "Alaska"
        
        # Escribir un mensaje indicando que se ha seleccionado Alaska
        st.write("Has seleccionado: Alaska")

    # Crear un botón con texto "Prueba con Medellín" y ancho de 200 píxeles
    if st.sidebar.button("Prueba con Medellín"):
        # Asignar "Medellín" a la ubicacion si se hace clic en el botón
        ubicacion = "Medellín"
        
        # Escribir un mensaje indicando que se ha seleccionado Medellín
        st.write("Has seleccionado: Medellín")
        
    # Crear un botón con texto "Prueba con Ushuaia" y ancho de 200 píxeles
    if st.sidebar.button("Prueba con Ushuaia"):
        # Asignar "Ushuaia" a la ubicacion si se hace clic en el botón
        ubicacion = "Ushuaia"
        
        # Escribir un mensaje indicando que se ha seleccionado Ushuaia
        st.write("Has seleccionado: Ushuaia")

    if ubicacion:
        # Escribir un mensaje indicando que se está buscando la ubicación
        st.write(f"Buscando la ubicación: {ubicacion}")
        
        # Obtener las coordenadas de la ubicación
        coordenadas = gpd.tools.geocode(ubicacion,
                          provider='nominatim', 
                          user_agent="ClimaApp")
        
        # Probar si se pueden obtener las coordenadas
        try:
            coordenadas = gpd.tools.geocode(ubicacion).geometry.values[0]
        except Exception as e:
            st.error(f"Error al obtener las coordenadas: {e}")
            return None
        
        # Encontrar el índice del punto más cercano
        punto_cercano, distancia = indice_espacial.nearest(coordenadas, 
                                                   return_all=False, 
                                                   return_distance=True)
        
        # Obtener la fila correspondiente en el DataFrame original
        fila_encontrada = df.loc[punto_cercano[1]]

        # Obtener del DataFrame la temperatura más cercana al punto de búsqueda
        try:
            temperatura_cercana = fila_encontrada['temp_mes'].values[0]
        except Exception as e:
            st.error("No se tienen datos sobre ese lugar")
            return e 
        
        # Definir emoticon según la temperatura del punto más cercano
        emoticon1, emoticon2 = definir_emoticon(temperatura_cercana)
        
        # Espacio para imprimir la temperatura promedio
        st.header("Temperatura promedio en el mes de abril es de ")
        
        # Imprimir la temperatura promedio
        st.header(f"{emoticon1} {temperatura_cercana} °C {emoticon2}")
        

def definir_emoticon(temperatura):
    """
    Función para definir los emoticon según la temperatura.

    Args:
        temperatura (float): Temperatura en grados Celsius.

    Returns:
        emoticon1 (str): Emoticon en relación a la temperatura.
        emoticon2 (str): Emoticon en relacion a la temperatura.
    """
    # Definir emoticon según la temperatura
    # Si la temperatura es mayor o igual a 25, hace calor
    if temperatura >= 25:
        emoticon1 = "🔥"
        emoticon2 = "🌡️"
    # Si la temperatura es mayor o igual a 15, está fresco
    elif temperatura >= 15:
        emoticon1 = "🌤️"
        emoticon2 = "☔"
    # Si la temperatura es mayor o igual a 5, está frío
    elif temperatura >= 5:
        emoticon1 = "❄️"
        emoticon2 = "🌧️"
    # Si la temperatura es menor a 5, hace mucho frío
    else:
        emoticon1 = "🧊"
        emoticon2 = "☃️"

    # Devolver los emoticones
    return emoticon1, emoticon2


if __name__ == "__main__":
    # Definir el servicio de geocodificación
    servicio_geocoder = Nominatim(user_agent="ClimaApp")
    
    # Llamar a la función principal
    main()

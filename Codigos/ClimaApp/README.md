# [ClimaApp 🌤️🌡️](https://climaapp.streamlit.app/)
ClimaApp es una aplicación básica de clima que te permite consultar la temperatura promedio del mes de abril en todo el mundo.

## ¿Qué hay en la carpeta?

- limpiar_datos.py: En este archivo se limpian los datos del [archivo original](https://github.com/spalominor/ClimaApp/blob/main/temp_mensual_espacial_p.csv), se eliminan columnas innecesarias, datos nulos o duplicados, y se convierten a un dataframe de temperaturas que se guarda como un [archivo nuevo](https://github.com/spalominor/ClimaApp/blob/main/temperatura.csv)
- indexar.py: Este archivo crea el índice espacial a partir de la columna "geom" del [archivo nuevo](https://github.com/spalominor/ClimaApp/blob/main/temperatura.csv)
- vista.py: Este archivo define la vista de la aplicación. Importa el índice espacial y el dataframe de las temperaturas. Obtiene la geocodificación y llama a los respectivos métodos para mostrar la respuesta

## Funcionalidades
- Consultar la temperatura promedio del mes de abril de cualquier país, ciudad o dirección.
- Interfaz fácil de usar con una barra lateral para seleccionar o buscar ubicaciones.
- Visualización clara de la temperatura promedio del mes de abril en la ubicación seleccionada.

## ¿Cómo funciona?

- Selección de Ubicación: En la barra lateral, puedes elegir un país, ciudad o introducir una dirección para consultar la temperatura promedio del mes de abril alrededor de esa ubicación.

- Obtención de Datos: Los datos se obtienen del [Global Climate Monitor](https://www.globalclimatemonitor.org/#), a partir de un archivo CSV que contenía, entre otras cosas, coordenadas geográficas y la medición promedio de temperatura en el mes de abril de 2023. Inicialmente, se contaba con más de 800,000 filas de datos, las cuales fueron limpiadas para obtener 65,000 filas de información relevante.

- Creación de Índice Espacial: Se crea un índice espacial STRtree utilizando geopandas, para facilitar la búsqueda de la temperatura más cercana a la ubicación consultada.

- Consulta de Temperatura: Cuando el usuario realiza una consulta, la ubicación se geocodifica en coordenadas utilizando el servicio de Nominatim y geopandas. Posteriormente, estas coordenadas se utilizan para buscar en el índice espacial y se devuelve la temperatura del punto más cercano a la ubicación consultada.


## Advertencia

- Esta aplicación provee datos aproximados de la temperatura promedio del mes de abril del año 2023 alrededor del mundo.
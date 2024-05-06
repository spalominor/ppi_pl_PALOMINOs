# [USPopulation 🗽📈](https://uspopulation.streamlit.app/)

Población estimada de los Estados Unidos de América por estado desde 2010 hasta 2023. US Population es un tablero interactivo desplegado en una aplicación web que proporciona información sobre la población de cada estado de los Estados Unidos.

## Funcionalidades

- **Selección de Año**: En la barra lateral, se puede elegir un año específico para visualizar la información de la población de ese año.
- **Mapa de Calor**: Se muestra un mapa de calor de los Estados Unidos que representa la distribución de la población en cada estado.
- **Información Relevante**: Se proporciona información adicional, como el crecimiento poblacional, el crecimiento porcentual, el estado con mayor crecimiento y decrecimiento, etc.
- **DataFrame**: Se muestra un DataFrame con la información detallada de la población de todos los estados.

## ¿Cómo funciona?

1. **Selección de Año:** El usuario selecciona un año de interés en la barra lateral.
  
2. **Obtención de Datos:** Los datos se obtienen de la página oficial del censo de los Estados Unidos, [Census](https://www.census.gov/data/tables/time-series/demo/popest/2020s-state-total.html). Se utilizan dos archivos CSV, uno que contiene la población entre 2010 y 2019, y otro que contiene la población entre 2020 y 2023. Estos datos se limpian, se unen y se organizan para su posterior visualización en el panel.

3. **Visualización en el Panel:** Después de procesar los datos, se muestra un panel interactivo que incluye el mapa de calor de los Estados Unidos con la distribución de la población, junto con información relevante como el crecimiento poblacional, el crecimiento porcentual, el estado con mayor crecimiento y decrecimiento, y un DataFrame con información detallada de la población de todos los estados.

## ¿Qué hay en el repositorio?

- limpiar_datos.py: En este archivo se limpian los datos y se crea un [archivo nuevo](https://github.com/spalominor/USPopulation/blob/main/us-population.csv) a partir de los csv de la población obtenidos de la pagína web [Census](https://www.census.gov/).
- utils.py: Contiene un diccionario y una lista útil para limpiar y organizar los datos
- graficas.py: Contiene la función que crea y retorna el mapa de calor de los Estados Unidos. Hecho con [plotly](https://plotly.com/python/)
- vista.py: Define la vista de la aplicación. Maneja la entrada del año. Importa el gráfico del mapa de calor.
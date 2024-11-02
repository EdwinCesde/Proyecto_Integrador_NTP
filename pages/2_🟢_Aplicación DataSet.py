import streamlit as st
import pandas as pd
import requests

st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")

df = pd.read_csv('./static/datasets/ventas.csv')


tad_descripcion, tab_Análisis_Exploratorio, tab_Filtrado_Básico, tab_Filtro_Final_Dinámico = st.tabs(["Descripción", "Análisis Exploratorio", "Filtrado Básico", "Filtro Final Dinámico"])

#----------------------------------------------------------
#Generador de datos
#----------------------------------------------------------
with tad_descripcion:      

    st.markdown('''
    ## Plantilla Básica para Proyecto Integrador

    ### Introducción

    -   ¿Qué es el proyecto?
    -   ¿Cuál es el objetivo principal?
    -   ¿Por qué es importante?

    ### Desarrollo

    -   Explicación detallada del proyecto
    -   Procedimiento utilizado
    -   Resultados obtenidos

    ### Conclusión

    -   Resumen de los resultados
    -   Logros alcanzados
    -   Dificultades encontradas
    -   Aportes personales
    ''')    

#----------------------------------------------------------
#Analítica 1
#----------------------------------------------------------
with tab_Análisis_Exploratorio:    
    st.title("Análisis Exploratorio")
    # Definir la URL de la API y parámetros
    url = "https://www.datos.gov.co/resource/ha6j-pa2r.json"
    params = {
        "$limit": 80000,   # Establece el límite en 80,000 registros
        "$offset": 0
    }

    # Obtener los datos desde la API
    response = requests.get(url, params=params)
    if response.status_code == 200:
        datos_json = response.json()
    else:
        st.error("Error al obtener los datos de la API.")
        datos_json = []

    # Convertir los datos a DataFrame
    df = pd.DataFrame.from_records(datos_json)

    # Título de la Aplicación
    st.title("Exploración de Datos del Dataset")

    # Mostrar primeras 5 filas del DataFrame
    st.subheader("Primeras 5 filas del DataFrame")
    st.write(df.head())

    # Mostrar cantidad de filas y columnas
    st.subheader("Cantidad de filas y columnas")
    st.write(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}")

    # Mostrar tipos de datos de cada columna
    st.subheader("Tipos de datos de cada columna")
    st.write(df.dtypes)

    # Identificar y mostrar columnas con valores nulos
    st.subheader("Columnas con valores nulos")
    st.write(df.isnull().sum())

    # Mostrar resumen estadístico de las columnas numéricas
    st.subheader("Resumen estadístico de columnas numéricas")
    st.write(df.describe())

    # Tabla con la frecuencia de valores únicos en una columna categórica
    st.subheader("Frecuencia de valores únicos")
    columna_categorica = st.selectbox("Selecciona una columna categórica:", df.select_dtypes(include="object").columns)
    st.write(df[columna_categorica].value_counts())

    # Otra información importante - Agrega aquí según tus necesidades
    st.subheader("Otra Información")
    st.write("Esta sección puede incluir gráficos, insights adicionales o análisis específicos.")
    
#----------------------------------------------------------
#Analítica 2
#----------------------------------------------------------
with tab_Filtrado_Básico:
        st.title("Filtro Básico")
        st.markdown("""
        * Permite filtrar datos usando condiciones simples. **(df[df['columna'] == 'valor'])**
        * Permite seleccionar una columna y un valor para el filtro. **(st.selectbox, st.text_input)**
        * Permite elegir un operador de comparación (igual, diferente, mayor que, menor que). **(st.radio)**
        * Muestra los datos filtrados en una tabla. **(st.dataframe)** 
        """)

#----------------------------------------------------------
#Analítica 3
#----------------------------------------------------------
with tab_Filtro_Final_Dinámico:
        st.title("Filtro Final Dinámico")
        st.markdown("""
        * Muestra un resumen dinámico del DataFrame filtrado. 
        * Incluye información como los criterios de filtrado aplicados, la tabla de datos filtrados, gráficos y estadísticas relevantes.
        * Se actualiza automáticamente cada vez que se realiza un filtro en las pestañas anteriores. 
        """)



    





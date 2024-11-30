import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests



st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")

df = pd.read_csv('./static/datasets/homicidios_trancito.csv') # DATAFRAME


tad_descripcion, tab_Análisis_Exploratorio, tab_Filtrado_Básico, tab_Filtro_Final_Dinámico = st.tabs(["Descripción", "Análisis Exploratorio", "Filtrado Básico", "Filtro Final Dinámico"])

#----------------------------------------------------------
#Generador de datos
#----------------------------------------------------------
with tad_descripcion:      

    st.markdown('''
    ## Homicidios accidente de tránsito Policía Nacional

    ### Introducción

    -   ¿Qué es el proyecto?
        Este proyecto presenta un análisis de datos relacionados con homicidios por accidentes de tránsito en la nación, cubriendo el periodo del 1 de enero de 2010 al 31 de octubre de 2024. La ciudadanía puede acceder a esta información para comprender patrones, tendencias y características de estos incidentes.

    -   ¿Cuál es el objetivo principal?
        El objetivo principal es facilitar el acceso y la comprensión de datos históricos sobre homicidios en accidentes de tránsito, proporcionando herramientas analíticas que permitan identificar tendencias y posibles factores de riesgo.
        
    -   ¿Por qué es importante?
        Democratiza el acceso a datos públicos, promueve el uso de datos para la toma de decisiones y políticas, facilita la identificación de factores críticos de accidentes.

    ### Desarrollo

    -   Explicación detallada del proyecto:
        Framework: Streamlit (rápido y fácil de usar para crear dashboards).
        Funcionalidades: Filtros interactivos, gráficos dinámicos y tablas.
    -   Procedimiento utilizado:
        Phyton con librerias streamlit, pandas,firebase y generador de texto con Gemini IA
        
    -   Resultados obtenidos:
        Página web funcional para análisis de datos en tiempo real.
        Visualizaciones intuitivas para el usuario final.
        


    ### Conclusión

    -   Resumen de los resultados
    -   Logros alcanzados:
        El frontend consume los datos del backend, los visualiza y permite a los usuarios interactuar con filtros.
    -   Dificultades encontradas:
        sincronización entre backend y frontend.
        Optimización de consultas para manejar grandes volúmenes de datos.
    -   Aportes personales:
        Diseño de una interfaz clara y accesible.
        Optimización del backend para consultas dinámicas.
    ''')    

#----------------------------------------------------------
#Analítica 1
#----------------------------------------------------------
with tab_Análisis_Exploratorio:    

    st.title("Análisis Exploratorio")
    #primeras 5 filas  
    st.title('Muestra las primeras 5 filas del DataFrame.')
    st.dataframe(df.head())
    #Cantidad de filas y columnas 
    st.title('Muestra la cantidad de filas y columnas del DataFrame')
    st.dataframe(df.shape)
    # Tipos de datos
    st.title('Muestra los tipos de datos de cada columna.')
    st.dataframe(df.dtypes)
    #Identifica y muestra las columnas con valores nulos
    st.title('Identifica y muestra las columnas con valores nulos.')
    st.dataframe((df.isnull().sum()))
    #Resumen estadístico de las columnas
    st.title('Muestra un resumen estadístico de las columnas numéricas.')
    st.dataframe(df.describe().drop(columns=['CODIGO DANE']))
    #//////////////////////////////////////////////////////////
    columna_categorica = 'ARMAS MEDIOS'  # Cambia esto por el nombre de tu columna

    # Calcular las frecuencias de valores únicos
    frecuencias = df[columna_categorica].value_counts()

    # Mostrar en Streamlit
    st.write(f"Frecuencia de valores únicos en la columna '{columna_categorica}':")
    st.dataframe(frecuencias.reset_index().rename(columns={'index': 'Valor', columna_categorica: 'Frecuencia'}))

#----------------------------------------------------------
#Analítica 2
#----------------------------------------------------------
with tab_Filtrado_Básico:
        st.title("Filtro Básico")
        st.title("Análisis Exploratorio")
    #     Definir la URL de la API y parámetros
    #    Hacerlo desde el csv 
        
        # Agregar un sidebar para los filtros
        st.header('Filtros') # realizar filtros
        """
        filtro_dpto = st.multiselect(
            'DEPARTAMENTO', df['DEPARTAMENTO'].unique()  # Asegúrate que el nombre de la columna es correcto
        )

        filtro_genero = st.multiselect(
            'GENERO', df['GENERO'].unique()  # Asegúrate que el nombre de la columna es correcto
        )

        filtro_grupo = st.multiselect(
            'GRUPO ETARÍO', df['GRUPO ETARÍO'].unique()  # Asegúrate que el nombre de la columna es correcto
        )

        # Filtrar los datos
        df_filtro = df.copy()
        if filtro_dpto:
            df_filtro = df_filtro[df_filtro['DEPARTAMENTO'].isin(filtro_dpto)]
        if filtro_genero:
            df_filtro = df_filtro[df_filtro['GENERO'].isin(filtro_genero)]
        if filtro_grupo:
            df_filtro = df_filtro[df_filtro['GRUPO ETARÍO'].isin(filtro_grupo)]

        st.bar_chart()
        

        # Mostrar el DataFrame filtrado
        st.dataframe(df_filtro)
        """

#----------------------------------------------------------
#Analítica 3
#----------------------------------------------------------
with tab_Filtro_Final_Dinámico:
        st.title("Filtro Final Dinámico")


        st.title("Municipios por departamento")
        st.write("Por favor seleccione el departamento y luego busque el municipio para visualizar los datos")
        departamento_seleccionado = st.selectbox("DEPARTAMENTO", df["DEPARTAMENTO"].unique())

        # Filtrar los municipios correspondientes al departamento seleccionado
        municipios_disponibles = df[df["DEPARTAMENTO"] == departamento_seleccionado]["MUNICIPIO"].unique()
        
        #Filtro para seleccionar Municipio del departamento seleccionado
        municipio = st.multiselect("Municipios", municipios_disponibles)

        # Filtrar el DataFrame con base en los municipios seleccionados (si no seleccionan, muestra todos los del departamento)
        if municipio:
            if municipio:
                df_filtro = df[(df["DEPARTAMENTO"] == departamento_seleccionado) & 
                                (df["MUNICIPIO"].isin(municipio))]
                if not df_filtro.empty:
                    conteo_municipios = df_filtro['MUNICIPIO'].value_counts()
                    fig, ax = plt.subplots(figsize=(10, 6))
                    conteo_municipios.plot(kind='bar', color='skyblue', ax=ax)
                    ax.set_title("Distribución de Registros por Municipio", fontsize=16)
                    ax.set_xlabel("Municipio", fontsize=12)
                    ax.set_ylabel("Cantidad de Registros", fontsize=12)
                    ax.tick_params(axis='x', rotation=45)
                    ax.grid(axis='y', linestyle='--', alpha=0.7)

                    st.pyplot(fig)
                else:
                    st.warning("No hay datos disponibles para los criterios seleccionados")                
            else:
                df_filtro = df[df[df["DEPARTAMENTO"] == departamento_seleccionado]]
        else:
            st.write("Todos los campos son obligarios")  
              
        st.title("Cantidad de accidentes por Género")


        filtro_departamento = st.multiselect(
             "DEPARTAMENTO",
             df['DEPARTAMENTO'].unique()
        )

        filtro_vehiculo = st.multiselect(
              "VEHÍCULO",
              df['ARMAS MEDIOS'].unique()
        )

        filtro_genero = st.multiselect(
              "GÉNERO", 
              df['GENERO'].unique()
        )

        filtro_grupo = st.multiselect(
            'GRUPO ETARÍO', 
            df['GRUPO ETARÍO'].unique()  
        )

        df_filtrado = df.copy()
        if filtro_departamento:
            df_filtrado = df_filtrado[df_filtrado["DEPARTAMENTO"].isin(filtro_departamento)]
        if filtro_vehiculo:
            df_filtrado = df_filtrado[df_filtrado["ARMAS MEDIOS"].isin(filtro_vehiculo)]
        if filtro_genero:
            df_filtrado = df_filtrado[df_filtrado["GENERO"].isin(filtro_genero)] 
        if filtro_grupo:
            df_filtrado = df_filtrado[df_filtrado["GRUPO ETARÍO"].isin(filtro_grupo)]
   
        fig, ax = plt.subplots()
        for grupo in df_filtrado["GRUPO ETARÍO"].unique():
            data = df_filtrado[df_filtrado["GRUPO ETARÍO"] == grupo]
            ax.hist(data["GENERO"], bins=10, alpha=0.5, label=grupo)

        ax.set_xlabel('Género')
        ax.set_ylabel('Cantidad')
        ax.legend(title='Grupo Etario')

        st.pyplot(fig)

        fig, ax = plt.subplots()
        for grupo in df_filtrado["ARMAS MEDIOS"].unique():
            data = df_filtrado[df_filtrado["ARMAS MEDIOS"] == grupo]
            ax.hist(data["GENERO"], bins=10, alpha=0.5, label=grupo)

        ax.set_xlabel('Género')
        ax.set_ylabel('Cantidad')
        ax.legend(title='Vehículo')

        st.pyplot(fig)

        st.title("Accidentes por Departamento")

        acc_dto = df['DEPARTAMENTO'].value_counts()

        st.bar_chart(acc_dto)
        st.markdown("""
        * Muestra un resumen dinámico del DataFrame filtrado. 
        * Incluye información como los criterios de filtrado aplicados, la tabla de datos filtrados, gráficos y estadísticas relevantes.
        * Se actualiza automáticamente cada vez que se realiza un filtro en las pestañas anteriores. 
        """)

        acc_mpio = df['GRUPO ETARÍO'].value_counts()
        st.bar_chart(acc_mpio)

    





import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests



st.set_page_config(layout="wide")

st.subheader("Análisis y Filtrado de Datos")

df = pd.read_csv('./static/datasets/homicidios_trancito.csv') # DATAFRAME


tad_descripcion, tab_Análisis_Exploratorio, tab_Filtro_Final_Dinámico = st.tabs(["Descripción", "Análisis Exploratorio", "Filtro Final Dinámico"])

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
                st.write("Datos filtrados", df_filtro)
            else:
                df_filtro = df[df[df["DEPARTAMENTO"] == departamento_seleccionado]]
        else:
            st.write("Todos los campos son obligarios")  
                  
        #st.write("Datos filtrados", df_filtro)

        

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
            df_filtrado = df_filtrado[df_filtrado["GRUPO ETARIO"].isin(filtro_grupo)]
   
        fig, ax = plt.subplots()
        for grupo in df_filtrado["GRUPO ETARÍO"].unique():
            data = df_filtrado[df_filtrado["GRUPO ETARÍO"] == grupo]
            ax.hist(data["GENERO"], bins=10, alpha=0.5, label=grupo)

        ax.set_xlabel('Género')
        ax.set_ylabel('Cantidad')
        ax.legend(title='Grupo Etario')

        st.pyplot(fig)

        st.title("Cantidad de accidentes por género y vehículo")

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
        
        st.title("Accidentes por Grupo etario")
        acc_mpio = df['GRUPO ETARÍO'].value_counts()
        st.bar_chart(acc_mpio)

        

    





import random
from faker import Faker
import streamlit as st 
import pandas as pd  
import firebase_admin  
from firebase_admin import credentials, firestore  
from typing import List
from datetime import datetime, timedelta

st.set_page_config(layout="wide")

st.subheader("Proyecto Integrador")

# Verificar si ya existe una instancia de la aplicación
if not firebase_admin._apps:  
    # Cargar las credenciales de Firebase desde los secretos de Streamlit
    firebase_credentials = st.secrets["FIREBASE_CREDENTIALS"]  
    # Convertir las credenciales a un diccionario Python
    secrets_dict = firebase_credentials.to_dict()  
    # Crear un objeto de credenciales usando el diccionario 
    cred = credentials.Certificate(secrets_dict)  
    # Inicializar la aplicación de Firebase con las credenciales
    app = firebase_admin.initialize_app(cred)

# Obtener el cliente de Firestore
db = firestore.client()


tad_descripcion, tab_Generador, tab_datos, tab_Análisis_Exploratorio, tab_Filtrado_Básico, tab_Filtro_Final_Dinámico = st.tabs(["Descripción", "Generador de datos", "Datos", "Análisis Exploratorio", "Filtrado Básico", "Filtro Final Dinámico"])

#----------------------------------------------------------
#Generador de datos
#----------------------------------------------------------
with tad_descripcion:      

    st.markdown('''   

    ### Introducción

    ### ¿Qué es el proyecto?
     La plataforma Análisis Confereasy es una solución  enfocada a la  lectura y análisis de datos clave de sus clientes, quienes buscan salas para conferencias, capacitaciones y espacios para eventos. A través de esta herramienta, Confereasy  obtiene una visión profunda de los comportamientos y preferencias de sus usuarios, permitiendo una mejora continua en sus servicios.          
    ### ¿Cuál es el objetivo principal?
    Generar hallazgos valiosos a partir del análisis de datos para que Confereasy pueda entender las preferencias y necesidades de sus clientes de manera profunda. Esto permite optimizar la gestión de sus espacios, adaptarse a las tendencias del mercado y ofrecer una experiencia que responda de manera más precisa a las expectativas de sus usuarios
    ### ¿Por qué es importante?
    La plataforma es crucial para Confereasy ya que facilita un enfoque basado en datos para la toma de decisiones. Al entender mejor las necesidades y comportamientos de sus clientes, Confereasy puede adaptarse de manera más eficiente a las demandas del mercado, mejorar sus servicios y fortalecer su propuesta de valor. Además, el análisis de datos permite identificar áreas de oportunidad y anticipar tendencias, lo que coloca a Confereasy en una posición de ventaja competitiva en el sector de alquiler de espacios para eventos y capacitaciones.

    ### Desarrollo

    ### Explicación detallada del proyecto
    La Plataforma de Análisis de Datos de Confereasy es un sistema interactivo de análisis diseñado para gestionar y evaluar los datos generados por los clientes y eventos en los espacios de Confereasy. Utilizando Python para el procesamiento y análisis de datos, la plataforma emplea tecnologías como Firebase para el almacenamiento en la nube, Streamlit para la creación de una interfaz visual e interactiva, y GitHub para el control de versiones y la colaboración. Con esta plataforma, Confereasy puede visualizar y analizar información clave como la tasa de ocupación de sus salas, la preferencia por tipos de eventos, la duración promedio de las reservas, y patrones de uso, entre otros datos. La implementación de Pandas en el proyecto permite el manejo y procesamiento de grandes conjuntos de datos, facilitando el análisis profundo y la generación de reportes personalizados.
                
    ### Procedimiento utilizado
    -  Recopilación de datos: Se recolectan datos de eventos y reservas a través del sistema de Confereasy, y estos datos se almacenan en Firebase, asegurando que estén disponibles en tiempo real y sean accesibles desde la nube.
    -  Procesamiento y análisis de datos: Con Python y Pandas, los datos se limpian, procesan y organizan para facilitar su interpretación. Se aplican diversas técnicas de análisis para identificar tendencias y patrones específicos relevantes para la gestión de eventos.
    -  Desarrollo de la interfaz con Streamlit: Se crea una interfaz visual con Streamlit que permite a los usuarios explorar los datos mediante gráficos interactivos, tablas y filtros. Esta interfaz facilita el acceso y análisis de la información, permitiendo realizar consultas y generar reportes específicos.
    -  Control de versiones y colaboración en GitHub: GitHub se utiliza para almacenar y gestionar el código de la plataforma, permitiendo el  seguimiento de cambios y la colaboración entre los desarrolladores.
    -  Visualización y generación de reportes: Se diseñan visualizaciones intuitivas para que el equipo de Confereasy pueda interpretar fácilmente los resultados. Estas visualizaciones pueden exportarse como reportes en diferentes formatos, facilitando la presentación de información para la toma de decisiones.

    ### Conclusión

    -   Resumen de los resultados
    -   Logros alcanzados
    -   Dificultades encontradas
    -   Aportes personales
    ''')

#----------------------------------------------------------
#Generador de datos
#----------------------------------------------------------
    st.write('Esta función Python genera datos ficticios de usuarios y productos y los carga en una base de datos Firestore, proporcionando una interfaz sencilla para controlar la cantidad de datos generados y visualizar los resultados.')
    # Inicializar Faker para Colombia
    fake = Faker('es_CO')

    #Lista de nacionalidades
    nacionalidades = [
    "Argentina", "Brasil", "Canadiense", "Chileno", "Colombiano",
    "Cubano", "Francés", "Alemán", "Español", "Estadounidense",
    "Italiano", "Mexicano", "Peruano", "Inglés", "Japonés",
    "Chino", "Indio", "Ruso", "Sueco", "Sudafricano"
]


    profesiones: List[str] = [
        "Ingeniero", "Médico", "Profesor", "Abogado", "Arquitecto",
        "Artista", "Cocinero", "Escritor", "Músico", "Piloto",
        "Científico", "Veterinario", "Desarrollador de software", "Contador", "Diseñador gráfico",
        "Electricista", "Carpintero", "Farmacéutico", "Físico", "Psicólogo", "Gerente de Proyectos",
        "Director de Marketing", "Consultor de Negocios", "Abogado Corporativo",
        "Analista Financiero", "Ejecutivo de Ventas", "Director de Recursos Humanos", "Product Manager",
        "Emprendedor", "Director de Estrategia", "Coordinador de Alianzas", "Responsable de Desarrollo de Negocios",
        "Asesor Legal", "Gerente de Operaciones", "Director de Tecnología (CTO)"
]

    salon: List[str] = [
        'Auditorio', 'Salon social', 'Penhouse', ''
]

    categorias: List[str] = [
        "Cumpleaños",
        "Bodas",
        "Aniversarios",
        "Graduaciones",
        "Fiestas temáticas",
        "Baby showers",
        "Fiestas de despedida",
        "Fiestas de fin de año",
        "Halloween",
        "Fiestas corporativas",
        "Fiestas de verano",
        "Fiestas de inauguración",
        "Fiestas de caridad",
        "Picnics"
]
def random_date(start: datetime, end: datetime) -> datetime:
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)

auxiliar = []
def generate_fake_users(n):
    users = []
    aforo = int 
    for _ in range(n):
        salon_seleccionado = random.choice(salon)
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2023, 12, 31)
        fecha_aleatoria = random_date(start_date, end_date)
        
        if salon_seleccionado == 'Auditorio':
            aforo = random.randint(50, 100)
        elif salon_seleccionado == 'Salon social':
            aforo = random.randint(1, 40)

        elif salon_seleccionado == 'Penhouse':
            aforo = random.randint(20, 50)
            
        user = {
            'nombre': fake.name(),
            'email': fake.email(),
            'edad': random.randint(18, 80),
            'nacionalidad': random.choice(nacionalidades),
            'profesiones': random.choice(profesiones),
            'celular': str(random.randint(3000000000, 3999999999)),
            'cedula': str(random.randint(1000000000, 1999999999)),
            'salon': salon_seleccionado,
            'categoria': random.choice(categorias),
            'ID Salon': salon_seleccionado,
            'asistentes': aforo,
            'fecha': fecha_aleatoria
    }   
        users.append(user)
    return users

def delete_collection(collection_name):
    docs = db.collection(collection_name).get()
    for doc in docs:
        doc.reference.delete()

def add_data_to_firestore(collection, data):
    for item in data:
        db.collection(collection).add(item)


with tab_Generador:
    st.write('Esta función Python genera datos ficticios de usuarios y productos y los carga en una base de datos Firestore, proporcionando una interfaz sencilla para controlar la cantidad de datos generados y visualizar los resultados.')
    
    with st.container(height=500):
        st.subheader('Usuarios')
        num_users = st.number_input('Número de usuarios a generar', min_value=1, max_value=1000, value=100)
        if st.button('Generar y Añadir Usuarios'):
            with st.spinner('Eliminando usuarios existentes...'):
                delete_collection('usuarios')
            with st.spinner('Generando y añadiendo nuevos usuarios...'):
                users = generate_fake_users(num_users)
                auxiliar = pd.DataFrame(users)
                add_data_to_firestore('usuarios', users)
            st.success(f'{num_users} usuarios añadidos a Firestore')
            st.dataframe(pd.DataFrame(users))


#----------------------------------------------------------
#Datos
#----------------------------------------------------------
with tab_datos:
    st.write('Esta función muestra datos de usuarios y productos almacenados en una base de datos Firestore, permitiendo una visualización organizada y fácil acceso a la información.')
    tab_user, tab_productos = st.tabs(["Usuarios", "Productos"])
    with tab_user:        
        # Obtener datos de una colección de Firestore
        users = db.collection('usuarios').stream()
        # Convertir datos a una lista de diccionarios
        users_data = [doc.to_dict() for doc in users]
        # Crear DataFrame
        df_users = pd.DataFrame(users_data)
        # Reordenar las columnas
        column_order = ['nombre', 'email', 'edad', 'ciudad']
        df_users = df_users.reindex(columns=column_order)   
        st.dataframe(df_users)

#----------------------------------------------------------
#Analítica 1
#----------------------------------------------------------
with tab_Análisis_Exploratorio:    
    st.title("Análisis Exploratorio")
    df =  pd.DataFrame(users_data)
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
    st.dataframe(df.describe())
    #//////////////////////////////////////////////////////////
    columna_categorica = 'categoria'  # Cambia esto por el nombre de tu columna

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
        st.header('Filtros') # realizar filtros
        filtro_nac = st.multiselect(
            'nacionalidad', df['nacionalidad'].unique()  # Asegúrate que el nombre de la columna es correcto
        )

        filtro_profesion = st.multiselect(
            'profesiones', df['profesiones'].unique()  # Asegúrate que el nombre de la columna es correcto
        )

        filtro_categoria = st.multiselect(
            'categoria', df['categoria'].unique()  # Asegúrate que el nombre de la columna es correcto
        )

        # Filtrar los datos
        df_filtro = df.copy()
        if filtro_nac:
            df_filtro = df_filtro[df_filtro['nacionalidad'].isin(filtro_nac)]
        if filtro_profesion:
            df_filtro = df_filtro[df_filtro['profesiones'].isin(filtro_profesion)]
        if filtro_categoria:
            df_filtro = df_filtro[df_filtro['categoria'].isin(filtro_categoria)]

        # Mostrar el DataFrame filtrado
        st.dataframe(df_filtro)

#----------------------------------------------------------
#Analítica 2
#----------------------------------------------------------
with tab_Filtro_Final_Dinámico:
        st.title("Filtro Final Dinámico")
        st.markdown("""
        * Muestra un resumen dinámico del DataFrame filtrado. 
        * Incluye información como los criterios de filtrado aplicados, la tabla de datos filtrados, gráficos y estadísticas relevantes.
        * Se actualiza automáticamente cada vez que se realiza un filtro en las pestañas anteriores. 
        """)
import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Mapping Demo", page_icon="🌍")


# Título y subtítulo
st.title("Proyecto Integrador: Análisis Confereasy")
st.subheader("Un Viaje Creativo con FourGroup")

# Imagen de fondo
image = Image.open("./static/proyecto.jpg") 
st.image(image, width=700, use_column_width=True)  

# Integrantes
st.header("Nuestro Equipo")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("./static/bro.jpg", width=200)  # Reemplaza con la ruta de la foto
    st.write("Esteban Giraldo")
    st.write("Data analyst Developer")

with col2:
    st.image("./static/Isaac.jpg", width=200)  # Reemplaza con la ruta de la foto
    st.write("Isaac Cano")
    st.write("Database Developer")

with col3:
    st.image("./static/Edwin.jpg", width=200)  # Reemplaza con la ruta de la foto
    st.write("Edwin Cárdenas")
    st.write("Graphics Developer")

with col4:
    st.image("./static/Mile.jpg", width=200)  # Reemplaza con la ruta de la foto
    st.write("Mileidy Henao")
    st.write("Fullstack Developer")

# Descripción del proyecto
st.header("Sobre el Proyecto")
st.write("La plataforma Análisis Confereasy es una solución  enfocada a la  lectura y análisis de datos clave de sus clientes, quienes buscan salas para conferencias, capacitaciones y espacios para eventos. A través de esta herramienta, Confereasy  obtiene una visión profunda de los comportamientos y preferencias de sus usuarios, permitiendo una mejora continua en sus servicios.")

st.header("Objetivo")
st.write("Generar hallazgos valiosos a partir del análisis de datos para que Confereasy pueda entender las preferencias y necesidades de sus clientes de manera profunda. Esto permite optimizar la gestión de sus espacios, adaptarse a las tendencias del mercado y ofrecer una experiencia que responda de manera más precisa a las expectativas de sus usuarios.")

st.header("Problemática que aborda")
st.write("En un mercado dinámico y competitivo, comprender a los clientes es clave para diferenciarse. Sin embargo, muchas empresas enfrentan dificultades para traducir los datos en conocimientos prácticos. Análisis Confereasy resuelve esta necesidad al ofrecer  análisis de datos, aportando claridad sobre los patrones de uso y preferencias de los clientes")

st.header("Enfoque")
st.write("Con un diseño  orientado a la recopilación de datos relevantes, Análisis Confereasy permite procesar información en tiempo real y transformarla en informes detallados que guían la toma de decisiones.")

# Más información
st.header("Más Información")

# Puedes añadir secciones como:
# - Tecnología utilizada
# - Resultados esperados
# - Presentación de resultados (fecha y formato)
# - Contacto para preguntas

st.write("Tecnologías Utilizadas: Python con librerías Streamlit, pandas.")

# Footer con links
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://www.google.com">Google</a> |
        <a href="https://www.facebook.com">Facebook</a> |
        <a href="https://www.linkedin.com">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)
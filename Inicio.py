import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Mapping Demo", page_icon="🌍")


# Título y subtítulo
st.title("Proyecto Integrador: Confereasy")
st.subheader("Un Viaje Creativo con FourGroup")

# Imagen de fondo
image = Image.open("./static/proyecto integrador.png") 
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
st.write("""
[Escribe aquí una breve descripción del proyecto, incluyendo el objetivo principal, la problemática que aborda y el enfoque que se utiliza. Puedes ser creativo y usar un lenguaje atractivo.]
""")

# Más información
st.header("Más Información")

# Puedes añadir secciones como:
# - Tecnología utilizada
# - Resultados esperados
# - Presentación de resultados (fecha y formato)
# - Contacto para preguntas

st.write("""
[Agrega la información adicional que consideres relevante.]
""")

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
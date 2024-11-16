import streamlit as st
import google.generativeai as genai
import PyPDF2
import os

# Configura la API Key de Google Generative AI
genai.configure(api_key=st.secrets.GEMINI.api_key)

# Selecciona el modelo Gemini 1.5
model = genai.GenerativeModel("gemini-1.5-flash")

# Funciones para leer los archivos
def read_pdf(file_path):
    text = ""
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Función para generar el resumen con Gemini
def generate_summary_with_gemini(text):
    response = model.generate_content(f"Resumen detallado del siguiente texto:\n\n{text}")
    return response.text

# Interfaz Streamlit
st.title("Generador de Resúmenes con Gemini 1.5")
st.write("Carga un archivo de texto (.txt o .pdf) para generar un resumen detallado usando el modelo Gemini 1.5.")

# Carga del archivo
uploaded_file = st.file_uploader("Sube tu archivo PDF o TXT", type=["pdf", "txt"])

if uploaded_file is not None:
    # Guardar el archivo cargado temporalmente
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Leer el contenido del archivo
    if uploaded_file.type == "application/pdf":
        text = read_pdf(file_path)
    else:
        text = read_text(file_path)

    # Mostrar parte del texto original
    st.subheader("Texto original:")
    st.write(text[:1000])  # Muestra solo los primeros 1000 caracteres

    # Generar el resumen
    if text:
        summary = generate_summary_with_gemini(text)
        st.subheader("Resumen generado:")
        st.write(summary)
    
    # Limpiar el archivo temporal
    os.remove(file_path)

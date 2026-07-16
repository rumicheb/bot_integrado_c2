import pandas as pd
import re
from pypdf import PdfReader

def simular_inventario():
    datos = {
        "Articulo": ["Combustible", "Raciones", "Munición 7.62mm", "Baterías HF"],
        "Cantidad": [15, 120, 500, 2],
        "Umbral Mínimo": [30, 50, 1000, 3]
    }
    return pd.DataFrame(datos)

def procesar_ley_pdf(pdf_path):
    try:
        print(f"Procesando el PDF: {pdf_path}")
        reader = PdfReader(pdf_path)
        texto_completo = ""
        for pagina in reader.pages:
            texto_completo += pagina.extract_text() + "\n"
        chunks = re.split(r'(?=Artículo\s+\d+)', texto_completo)
        # Me devuelve una lista de chunks que tengan más de 60 caracteres,
        # eliminando espacios en blanco al inicio y al final
        return [chunk.strip() for chunk in chunks if len(chunk.strip()) > 60]
    except Exception as e:
        print(f"Error al procesar el PDF: {e}")
        return []
    
def buscar_articulo_vectorial(consulta_usuario:str):
    # Simulación de búsqueda vectorial
    # En un escenario real, aquí se implementaría la lógica de búsqueda vectorial
    # utilizando embeddings y un índice vectorial.
    articulos = procesar_ley_pdf("DL1137.pdf")
    if not articulos:
        return "No se pudo procesar el PDF de la ley.", 0.0
    
    # Simulación: devolver el primer artículo y una similitud aleatoria
    return articulos[0], 0.5  # Simulación de similitud
    

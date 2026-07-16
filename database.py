# database.py
import pandas as pd
import re
from pypdf import PdfReader


def simular_inventario():
    """Retorna un DataFrame con el estado de abastecimiento del PVF."""
    datos = {
        'Articulo': ['Combustible', 'Raciones', 'Munición 7.62mm', 'Baterías HF'],
        'Cantidad': [15, 120, 5000, 2],
        'Umbral_Minimo': [30, 50, 1000, 3]
    }
    return pd.DataFrame(datos)

def procesar_ley_pdf(pdf_path):
    """Extrae y segmenta por artículos el documento PDF proporcionado."""
    try:
        reader = PdfReader(pdf_path)
        texto_completo = ""
        for pagina in reader.pages:
            texto_completo += pagina.extract_text() + "\n"
        
        # Segmentación usando Regex por la palabra 'Artículo'
        chunks = re.split(r'(?=Artículo\s+\d+)', texto_completo)
        return [c.strip() for c in chunks if len(c.strip()) > 60]
    except Exception as e:
        print(f"❌ Error leyendo PDF: {e}")
        return []

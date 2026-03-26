import os
import pandas as pd

def cargarDatos():
    script_dir = os.path.dirname(__file__)
    ruta = os.path.join(script_dir, "..", "Base_de_datos.xlsx")
    df = pd.read_excel(ruta)
    print(f"Datos cargados correctamente. Filas: {df.shape[0]}, Columnas: {df.shape[1]}")
    return df

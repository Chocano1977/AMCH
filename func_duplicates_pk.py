import pandas as pd

def obtener_duplicados_por_campo(df, campo):
    """
    Devuelve las filas del DataFrame que tienen valores duplicados en el campo especificado.
    """
    return df[df.duplicated(subset=[campo], keep=False)]

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'id': [1, 2, 2, 3, 4, 4, 4],
    'valor': ['a', 'b', 'c', 'd', 'e', 'f', 'g']
})

duplicados = obtener_duplicados_por_campo(df, 'id')
print(duplicados)
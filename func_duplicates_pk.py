import pandas as pd

def obtener_duplicados_por_campos(df, campos):
    """
    Devuelve las filas del DataFrame que tienen valores duplicados en la combinación de los campos especificados.
    """
    return df[df.duplicated(subset=campos, keep=False)]

# Crear un DataFrame de ejemplo
df = pd.DataFrame({
    'id': [1, 2, 2, 3, 4, 4, 4,4],
    'valor': ['a', 'b', 'c', 'd', 'e', 'f', 'g','g']
})

duplicados = obtener_duplicados_por_campos(df, ['id', 'valor'])
print(duplicados)
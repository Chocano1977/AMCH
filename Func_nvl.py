def nvl(valor, reemplazo):
    """
    Devuelve 'valor' si no es None, en caso contrario devuelve 'reemplazo'.
    Equivalente a la función NVL de Oracle.
    """
    return valor if valor is not None else reemplazo

# Ejemplo de uso:
#   print(nvl(None, 'sc'))  # Salida: sc
#   print(nvl(5, 'sc'))     # Salida: 5
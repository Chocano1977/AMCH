def generate_pk(*args):
    """
    Devuelve la concatenación de los argumentos recibidos, separados por '_'.
    """
    return "_".join(str(arg) for arg in args)

# ...existing code...

# Ejemplo de uso:
#   resultado = concatenar_campos(1, 20, "ABC")
#   print(resultado)  # Salida: 1_20_ABC
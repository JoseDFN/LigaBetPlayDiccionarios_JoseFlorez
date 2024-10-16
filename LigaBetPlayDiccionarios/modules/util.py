# Importa el módulo 'limpiar' y lo renombra como 'clp' para su uso en este script
import modules.limpiar as clp

# Define una función llamada 'vacio' que toma un parámetro 'src'
def vacio (src):
    # Comprueba si el parámetro 'src' es una cadena vacía
    if src == '':
            # Si 'src' está vacío, imprime un mensaje de error
            print("La variable no puede estar vacía.")
            # Llama a la función 'comandoPause()' del módulo 'clp'
            # Esto probablemente pausa la ejecución hasta que el usuario presione una tecla
            clp.comandoPause()
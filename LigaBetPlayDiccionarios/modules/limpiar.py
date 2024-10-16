# Importación de módulos necesarios
import platform
import subprocess

def ejecutar_comandoLimp():
    """Función para limpiar la pantalla de la consola."""
    # Obtiene el nombre del sistema operativo
    sistema_operativo = platform.system()
    
    # Ejecuta el comando apropiado según el sistema operativo
    if sistema_operativo == "Windows":
        # En Windows, usa 'cls' para limpiar la pantalla
        subprocess.run(['cls'], shell=True)
    elif sistema_operativo == "Linux" or sistema_operativo == "Darwin":
        # En Linux o macOS (Darwin), usa 'clear' para limpiar la pantalla
        subprocess.run(['clear'])
    else:
        # Si no es ninguno de los sistemas operativos soportados, lanza un error
        raise ValueError("Sistema operativo no soportado")

def comandoPause():
    """Función para pausar la ejecución del programa hasta que el usuario presione una tecla."""
    # Obtiene el nombre del sistema operativo
    sistema_operativo = platform.system()
    
    # Usa una estructura match-case para manejar diferentes sistemas operativos
    match sistema_operativo:
        case 'Windows':
            # En Windows, usa el comando 'pause'
            subprocess.run(['pause'], shell=True)
        case 'Linux':
            # En Linux, usa input() para pausar
            input('De enter o cualquier tecla para continuar......')
        case 'Darwin':
            # En macOS (Darwin), también usa input() para pausar
            input('De enter o cualquier tecla para continuar......')
        case _:
            # Si no es ninguno de los sistemas operativos soportados, lanza un error
            raise ValueError("Sistema operativo no soportado")
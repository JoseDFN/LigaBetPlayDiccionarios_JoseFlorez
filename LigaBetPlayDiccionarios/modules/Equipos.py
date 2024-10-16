# Importación de módulos necesarios
import copy
import modules.limpiar as clp
import modules.Menus as msg
import modules.Data as data

# Variable global para llevar el conteo de equipos
codigo = 0

def regEquipos(liga):
    """Función para registrar nuevos equipos en la liga."""
    global codigo
    while True:
        clp.ejecutar_comandoLimp()  # Limpia la pantalla
        print(msg.NombreEquipo)  # Muestra un mensaje (probablemente un título)
        codigo += 1
        nuevo_equipo = copy.deepcopy(data.equipos)  # Crea una copia del modelo de equipo

        try:
            # Solicita y valida el nombre del equipo
            nuevo_equipo['nombreEqu'] = input("Ingrese el nombre del equipo: ").strip()
            if not nuevo_equipo['nombreEqu']:
                raise ValueError("El nombre del equipo no puede estar vacío.")
        except ValueError as ve:
            print(ve)
            clp.comandoPause()
            continue

        # Agrega el nuevo equipo a la liga
        liga['Equipos'][codigo] = nuevo_equipo
        print(f"\nEquipo '{nuevo_equipo['nombreEqu']}' agregado con éxito (Código: {codigo}).")
        
        # Pregunta si se desea agregar otro equipo
        continuar = input("\n¿Desea agregar otro equipo? (S/N): ").upper()
        if continuar != 'S':
            break

    clp.comandoPause()

def mEquipo(liga):
    """Función para mostrar todos los equipos registrados en la liga."""
    clp.ejecutar_comandoLimp()  # Limpia la pantalla
    print("\nEquipos registrados:")
    if not liga['Equipos']:
        print("No hay equipos registrados.")
    else:
        for cod, equipo in liga['Equipos'].items():
            print(f"Código: {cod}, Nombre: {equipo['nombreEqu']}")
    clp.comandoPause()

def esEquipo(liga):
    """Función para mostrar información detallada de un equipo específico."""
    try:
        clp.ejecutar_comandoLimp()  # Limpia la pantalla
        print('Menú de Equipos:')
        for codigo, equipo in liga['Equipos'].items():
            print(f'{codigo}. {equipo["nombreEqu"]}')

        # Solicita el código del equipo
        codigo = int(input('Ingrese el código del equipo: '))

        # Verifica si el equipo existe
        if codigo not in liga['Equipos']:
            print('El código del equipo no existe.')
            clp.comandoPause()
            return

        equipo = liga['Equipos'][codigo]
        print(f"\nInformación del equipo '{equipo['nombreEqu']}':")
        print(f"Código: {codigo}")
        print("Plantel:")
        # ... (Código para mostrar el plantel)

        # Muestra las estadísticas del equipo
        print("Estadísticas del equipo:")
        for stat, value in equipo['estadisticas Equipo'].items():
            print(f"  {stat}: {value}")

        clp.comandoPause()
    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
        clp.comandoPause()
# Importación de módulos necesarios
import copy
import modules.limpiar as clp
import modules.Menus as msg
import modules.Data as data
import modules.Equipos as equip
import modules.regCompPlantel as regCplan

# Variable global para llevar el conteo de partidos
codigoPartido = int(0)

def addPartidos(liga):
    """Función para agregar nuevos partidos a la liga."""
    isAddPartidos = True
    while(isAddPartidos):
        try:
            clp.ejecutar_comandoLimp()  # Limpia la pantalla
            global codigoPartido
            codigoPartido += 1
            nuevoPartido = copy.deepcopy(data.partido)  # Crea una copia del modelo de partido
            
            # Captura de la fecha del partido
            dia = input('Ingrese el día: ')
            mes = input('Ingrese el mes: ')
            año = input('Ingrese el año: ')
            nuevoPartido['fecha'] = f'{año}-{mes}-{dia}'
            
            clp.ejecutar_comandoLimp()
            equip.mEquipo(liga)  # Muestra los equipos disponibles
            
            # Selección del equipo local
            try:
                equipolocal = int(input('Seleccione el equipo local: '))
                nuevoPartido['local'] = liga['Equipos'][equipolocal]['nombreEqu']
            except (ValueError, KeyError):
                print("Error: Selección de equipo local inválida.")
                continue

            # Selección del equipo visitante
            try:
                equipovisitante = int(input('Seleccione el equipo visitante: '))
                nuevoPartido['visitante'] = liga['Equipos'][equipovisitante]['nombreEqu']
            except (ValueError, KeyError):
                print("Error: Selección de equipo visitante inválida.")
                continue
            
            # Agrega el nuevo partido a la liga
            liga['Partidos'][codigoPartido] = nuevoPartido
            
            # Pregunta si se desea agregar otro partido
            continuar = input("\n¿Desea agregar otro partido? (S/N): ")
            if continuar.upper() != 'S':
                break
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
            clp.comandoPause()
    return

def viewPartidos(liga: dict):
    """Función para ver todos los partidos de la liga."""
    try:
        clp.ejecutar_comandoLimp()
        print('Partidos: ')
        for codigoPartido, partido in liga['Partidos'].items():
            print(f'{codigoPartido}. {partido["local"]} vs {partido["visitante"]} - {partido["fecha"]}')
    except KeyError as e:
        print(f"Error al acceder a los datos de los partidos: {e}")
    clp.comandoPause()

def regEstadisticasPartido(liga):
    """Función para registrar estadísticas de un partido."""
    while True:
        try:
            clp.ejecutar_comandoLimp()
            viewPartidos(liga)  # Muestra los partidos disponibles
            codigoPartido = int(input('Ingrese el código del partido: '))
            
            if codigoPartido not in liga['Partidos']:
                print('El código del partido no existe.')
                clp.comandoPause()
                continue
            else:
                while True:
                    opE = input('Ingrese 1 si quiere ingresar las estadísticas de Local y 2 si quiere ingresar las de Visitantes: ')
                    if not opE.isdigit() or int(opE) not in [1, 2]:
                        print('Opción inválida. Por favor, ingrese 1 o 2.\n')
                        continue

                    if int(opE) == 1:
                        try:
                            equip.mEquipo(liga)  # Muestra los equipos
                            equipolocal = int(input('Ingrese el equipo Local: '))
                            clp.ejecutar_comandoLimp()
                            regCplan.mostrarJ(liga)  # Muestra los jugadores
                            jugadorGol = int(input('Seleccione el jugador que hizo gol: '))
                            clp.ejecutar_comandoLimp()
                            cantidadGoles = int(input('Cuántos goles hizo el jugador? '))
                            # Actualiza las estadísticas del jugador y del partido
                            liga['Equipos'][equipolocal]['Plantel']['jugadores'][jugadorGol]['estadisticas']['golesAnotados'] += cantidadGoles
                            liga["Partidos"][codigoPartido]["golesLocal"] = liga["Partidos"][codigoPartido].get("golesLocal", 0) + cantidadGoles
                        except (ValueError, KeyError):
                            print("Error en el ingreso de datos para el equipo local.")
                            continue

                    elif int(opE) == 2:
                        try:
                            equip.mEquipo(liga)  # Muestra los equipos
                            equipovisitante = int(input('Ingrese el equipo Visitante: '))
                            clp.ejecutar_comandoLimp()
                            regCplan.mostrarJ(liga)  # Muestra los jugadores
                            jugadorGol = int(input('Seleccione el jugador que hizo gol: '))
                            clp.ejecutar_comandoLimp()
                            cantidadGoles = int(input('Cuántos goles hizo el jugador? '))
                            # Actualiza las estadísticas del jugador y del partido
                            liga['Equipos'][equipovisitante]['Plantel']['jugadores'][jugadorGol]['estadisticas']['golesAnotados'] += cantidadGoles
                            liga["Partidos"][codigoPartido]["golesVisitante"] = liga["Partidos"][codigoPartido].get("golesVisitante", 0) + cantidadGoles
                        except (ValueError, KeyError):
                            print("Error en el ingreso de datos para el equipo visitante.")
                            continue
                    
                    continuar = input("\n¿Desea agregar otro resultado? (S/N o cualquiera): ")
                    if continuar.upper() != 'S':
                        break

            continuar = input("\n¿Desea salir al menú principal? (N/S o cualquiera): ")
            if continuar.upper() != 'N':
                break
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}")
            clp.comandoPause()
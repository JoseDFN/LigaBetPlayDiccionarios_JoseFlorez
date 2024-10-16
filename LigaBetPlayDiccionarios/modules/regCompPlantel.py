import copy
import modules.limpiar as clp
import modules.Menus as msg
import modules.Data as data
import modules.Equipos as equip

# Variables globales para almacenar los códigos de diferentes miembros del equipo
codigoTec = int(0)
codigoATec = int(0)
codigoPrepFisico = int(0)
codigoCuerpoMedico = int(0)

# Función para registrar un jugador en un equipo
def regJugador(liga):
    while True:
        try:
            clp.ejecutar_comandoLimp()  # Limpia la pantalla o interfaz
            print("\nEquipos registrados:")
            # Muestra los equipos registrados
            for cod, equipo in liga['Equipos'].items():
                print(f"Código: {cod}, Nombre: {equipo['nombreEqu']}")
            # Solicita al usuario ingresar el código del equipo
            opEquipo = int(input('Ingrese el equipo del jugador: '))
            if opEquipo not in liga['Equipos']:
                print('El equipo no existe.')
                clp.comandoPause()
                continue

            # Genera un código para el nuevo jugador basado en la cantidad de jugadores registrados
            codigoJugador = len(liga['Equipos'][opEquipo]['Plantel']['jugadores']) + 1
            # Crea una copia del template de jugador para evitar modificar el original
            nuevo_Jugador = copy.deepcopy(data.jugador)
            # Solicita datos para el nuevo jugador
            nuevo_Jugador['dorsal'] = int(input('Ingrese el dorsal del jugador: '))
            nuevo_Jugador['posicion'] = input('Ingrese la posicion del jugador: ')
            nuevo_Jugador['nombre'] = input('Ingrese el nombre del jugador: ')
            # Registra el jugador en el plantel del equipo seleccionado
            liga['Equipos'][opEquipo]['Plantel']['jugadores'][codigoJugador] = nuevo_Jugador
            print(f"\nJugador '{nuevo_Jugador['nombre']}' agregado con éxito (Código: {codigoJugador}).")

            # Pregunta si se desea agregar otro jugador
            continuar = input("\n¿Desea agregar otro jugador? (S/N): ")
            if continuar.upper() != 'S':
                break
        # Manejo de errores
        except KeyError:
            print("Error: Equipo no encontrado.")
            clp.comandoPause()
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar un número.")
            clp.comandoPause()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            clp.comandoPause()

# Función para mostrar los jugadores de un equipo
def mostrarJ(liga):
    try:
        # Muestra los equipos registrados
        for cod, equipo in liga['Equipos'].items():
            print(f"Código: {cod}, Nombre: {equipo['nombreEqu']}")
        # Solicita el código del equipo del que se desea ver los jugadores
        opEquipo = int(input('Ingrese el equipo de los jugadores: '))
        print("\nJugadores registrados:")
        # Muestra los jugadores registrados en el equipo
        for cod, nJugador in liga['Equipos'][opEquipo]['Plantel']['jugadores'].items():
            print(f"Código: {cod}, Nombre: {nJugador['nombre']} con dorsal {nJugador['dorsal']}")
        clp.comandoPause()
    except KeyError:
        print("Error: Equipo o jugador no encontrado.")
        clp.comandoPause()
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar un número.")
        clp.comandoPause()
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        clp.comandoPause()

# Función para registrar estadísticas de un jugador
def regEsJugador(liga):
    try:
        clp.ejecutar_comandoLimp()  # Limpia la pantalla o interfaz
        mostrarJ(liga)  # Muestra los jugadores registrados
        # Solicita el código del jugador para registrar estadísticas
        opJugador = int(input('Ingrese el jugador a ingresar las estadísticas: '))
    except ValueError:
        print("Error: Entrada inválida.")
        clp.comandoPause()
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        clp.comandoPause()

# Función para registrar un técnico en un equipo
def regTecnico(liga):
    while True:
        try:
            # Muestra los equipos registrados
            for cod, equipo in liga['Equipos'].items():
                print(f"Código: {cod}, Nombre: {equipo['nombreEqu']}")
            # Solicita el código del equipo
            opEquipo = int(input('Ingrese el equipo del tecnico a registrar: '))
            if opEquipo not in liga['Equipos']:
                print('El equipo no existe.')
                clp.comandoPause()
                continue

            # Genera un código para el nuevo técnico
            codigoTec = len(liga['Equipos'][opEquipo]['Plantel']['tecnicos']) + 1
            # Crea una copia del template del técnico
            nuevo_Tecnico = copy.deepcopy(data.tecnico)
            nuevo_Tecnico['nombre'] = input('Ingrese el nombre del técnico: ')
            # Registra el técnico en el equipo seleccionado
            liga['Equipos'][opEquipo]['Plantel']['tecnicos'][codigoTec] = nuevo_Tecnico
            print(f"\nTecnico '{nuevo_Tecnico['nombre']}' agregado con éxito (Código: {codigoTec}).")

            # Pregunta si se desea agregar otro técnico
            continuar = input("\n¿Desea agregar otro Tecnico? (S/N): ")
            if continuar.upper() != 'S':
                break
        except KeyError:
            print("Error: Equipo no encontrado.")
            clp.comandoPause()
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar un número.")
            clp.comandoPause()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            clp.comandoPause()

# Función para registrar un asistente técnico en un equipo
def regAsisTecnico(liga):
    while True:
        try:
            # Muestra los equipos registrados
            for cod, equipo in liga['Equipos'].items():
                print(f"Código: {cod}, Nombre: {equipo['nombreEqu']}")
            # Solicita el código del equipo
            opEquipo = int(input('Ingrese el equipo del asistente tecnico a registrar: '))
            if opEquipo not in liga['Equipos']:
                print('El equipo no existe.')
                clp.comandoPause()
                continue

            # Genera un código para el nuevo asistente técnico
            codigoATec = len(liga['Equipos'][opEquipo]['Plantel']['asistentesTecnicos']) + 1
            # Crea una copia del template del asistente técnico
            nuevo_Tecnico = copy.deepcopy(data.asisrtenteTecnico)
            nuevo_Tecnico['nombre'] = input('Ingrese el nombre del asistente técnico: ')
            # Registra el asistente técnico en el equipo seleccionado
            liga['Equipos'][opEquipo]['Plantel']['asistentesTecnicos'][codigoATec] = nuevo_Tecnico
            print(f"\nAsistente Técnico '{nuevo_Tecnico['nombre']}' agregado con éxito (Código: {codigoATec}).")

            # Pregunta si se desea agregar otro asistente técnico
            continuar = input("\n¿Desea agregar otro asistente Técnico? (S/N): ")
            if continuar.upper() != 'S':
                break
        except KeyError:
            print("Error: Equipo no encontrado.")
            clp.comandoPause()
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar un número.")
            clp.comandoPause()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            clp.comandoPause()

# Función para registrar un preparador físico en un equipo
def regPrepFisico(liga):
    while True:
        try:
            # Muestra los equipos registrados
            for cod, equipo in liga['Equipos'].items():
                print(f"Código: {cod}, Nombre: {equipo['nombreEqu']}")
            # Solicita el código del equipo
            opEquipo = int(input('Ingrese el equipo del preparador físico a agregar: '))
            if opEquipo not in liga['Equipos']:
                print('El equipo no existe.')
                clp.comandoPause()
                continue

            # Genera un código para el nuevo preparador físico
            codigoPrepFisico = len(liga['Equipos'][opEquipo]['Plantel']['preparadoresfisicos']) + 1
            # Crea una copia del template del preparador físico
            nuevo_PrepFisico = copy.deepcopy(data.preparadorFisico)
            nuevo_PrepFisico['nombre'] = input('Ingrese el nombre del preparador físico: ')
            nuevo_PrepFisico['rol'] = input('Ingrese el rol del preparador físico: ')
            # Registra el preparador físico en el equipo seleccionado
            liga['Equipos'][opEquipo]['Plantel']['preparadoresfisicos'][codigoPrepFisico] = nuevo_PrepFisico
            print(f"\nPreparador Físico '{nuevo_PrepFisico['nombre']}' agregado con éxito (Código: {codigoPrepFisico}).")

            # Pregunta si se desea agregar otro preparador físico
            continuar = input("\n¿Desea agregar otro preparador físico? (S/N): ")
            if continuar.upper() != 'S':
                break
        except KeyError:
            print("Error: Equipo no encontrado.")
            clp.comandoPause()
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar un número.")
            clp.comandoPause()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            clp.comandoPause()

# Función para registrar un miembro del cuerpo médico en un equipo
def regCuerpoMedico(liga):
    while True:
        try:
            # Muestra los equipos registrados
            for cod, equipo in liga['Equipos'].items():
                print(f"Código: {cod}, Nombre: {equipo['nombreEqu']}")
            # Solicita el código del equipo
            opEquipo = int(input('Ingrese el equipo del cuerpo médico a agregar: '))
            if opEquipo not in liga['Equipos']:
                print('El equipo no existe.')
                clp.comandoPause()
                continue

            # Genera un código para el nuevo miembro del cuerpo médico
            codigoCuerpoMedico = len(liga['Equipos'][opEquipo]['Plantel']['cuerpoMedi']) + 1
            # Crea una copia del template del cuerpo médico
            nuevo_CuerpoMedico = copy.deepcopy(data.cuerpoMedico)
            nuevo_CuerpoMedico['nombre'] = input('Ingrese el nombre del cuerpo médico: ')
            nuevo_CuerpoMedico['rol'] = input('Ingrese el rol del cuerpo médico: ')
            # Registra el cuerpo médico en el equipo seleccionado
            liga['Equipos'][opEquipo]['Plantel']['cuerpoMedi'][codigoCuerpoMedico] = nuevo_CuerpoMedico
            print(f"\nCuerpo Médico '{nuevo_CuerpoMedico['nombre']}' agregado con éxito (Código: {codigoCuerpoMedico}).")

            # Pregunta si se desea agregar otro miembro del cuerpo médico
            continuar = input("\n¿Desea agregar otro integrante del cuerpo médico? (S/N): ")
            if continuar.upper() != 'S':
                break
        except KeyError:
            print("Error: Equipo no encontrado.")
            clp.comandoPause()
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar un número.")
            clp.comandoPause()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            clp.comandoPause()

# Función para registrar estadísticas de un jugador
def regEstadisticasJugador(liga):
    while True:
        try:
            equip.mEquipo(liga)  # Muestra los equipos registrados
            # Solicita el código del equipo del jugador
            opEquipo = int(input('Ingrese el equipo del jugador: '))
            if opEquipo not in liga['Equipos']:
                print('El equipo no existe.')
                clp.comandoPause()
                continue

            mostrarJ(liga)  # Muestra los jugadores registrados
            # Solicita el código del jugador para registrar estadísticas
            opJugador = int(input('Ingrese el jugador de las estadísticas: '))
            if opJugador not in liga['Equipos'][opEquipo]['Plantel']['jugadores']:
                print('El jugador no existe.')
                clp.comandoPause()
                continue

            # Solicita las estadísticas del jugador
            tAmarillas = int(input('Ingrese la cantidad de tarjetas amarillas del jugador: '))
            liga["Equipos"][opEquipo]["Plantel"]["jugadores"][opJugador]["estadisticas"]["tarjetasAmarillas"] += tAmarillas
            tRojas = int(input('Ingrese la cantidad de tarjetas rojas del jugador: '))
            liga["Equipos"][opEquipo]["Plantel"]["jugadores"][opJugador]["estadisticas"]["tarjetasRojas"] += tRojas
            tFaltas = int(input('Ingrese el total de faltas del jugador: '))
            liga["Equipos"][opEquipo]["Plantel"]["jugadores"][opJugador]["estadisticas"]["totalFaltas"] += tFaltas
            
            # Pregunta si se desea agregar otra estadística
            continuar = input("\n¿Desea agregar otra estadistica? (S/N o cualquiera): ")
            if continuar.upper() != 'S':
                break
        except KeyError:
            print("Error: Equipo o jugador no encontrado.")
            clp.comandoPause()
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar un número.")
            clp.comandoPause()
        except Exception as e:
            print(f"Se produjo un error inesperado: {e}")
            clp.comandoPause()

# Función para ver las estadísticas de un jugador
def verEstadisticasJugador(liga):
    try:
        equip.mEquipo(liga)  # Muestra los equipos registrados
        # Solicita el código del equipo del jugador
        opEquipo = int(input('Ingrese el equipo del jugador: '))
        if opEquipo not in liga['Equipos']:
            print('El equipo no existe.')
            clp.comandoPause()
            return  # Salir de la función si el equipo no existe

        mostrarJ(liga)  # Muestra los jugadores registrados
        # Solicita el código del jugador para ver sus estadísticas
        opJugador = int(input('Ingrese el código del jugador para ver las estadísticas: '))
        if opJugador not in liga['Equipos'][opEquipo]['Plantel']['jugadores']:
            print('El jugador no existe.')
            clp.comandoPause()
            return  # Salir de la función si el jugador no existe

        # Muestra las estadísticas del jugador
        estadisticas = liga['Equipos'][opEquipo]['Plantel']['jugadores'][opJugador]['estadisticas']
        print(f"\nEstadísticas del jugador '{liga['Equipos'][opEquipo]['Plantel']['jugadores'][opJugador]['nombre']}':")
        print(f"Tarjetas amarillas: {estadisticas['tarjetasAmarillas']}")
        print(f"Tarjetas rojas: {estadisticas['tarjetasRojas']}")
        print(f"Total de faltas: {estadisticas['totalFaltas']}")
        clp.comandoPause()

    except KeyError:
        print("Error: Equipo o jugador no encontrado.")
        clp.comandoPause()
    except ValueError:
        print("Error: Entrada inválida. Asegúrese de ingresar un número.")
        clp.comandoPause()
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
        clp.comandoPause()

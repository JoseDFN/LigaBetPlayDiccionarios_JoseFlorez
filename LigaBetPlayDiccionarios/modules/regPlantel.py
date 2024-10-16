import modules.limpiar as clp  # Módulo para limpiar la pantalla y pausar la ejecución.
import modules.Menus as msg  # Módulo que contiene menús para el programa.
import modules.regCompPlantel as regP  # Módulo para registrar el plantel del equipo.

def regPlantel(liga):
    """Función para registrar el plantel de un equipo"""
    
    isAllow = True  # Variable de control para mantener el ciclo de registro activo.
    
    # Bucle principal para mostrar el menú y registrar el plantel.
    while isAllow:
        clp.ejecutar_comandoLimp()  # Limpia la pantalla antes de mostrar el menú.
        print(msg.MenuRegPlantel)  # Muestra el menú para registrar el plantel.
        
        try:
            # Solicita al usuario que seleccione una opción del menú.
            op = int(input('Ingrese la opción: '))
        except ValueError:
            # Si el usuario ingresa algo que no sea un número, muestra un mensaje de error.
            print('Tipo de opción no válido. Debe ser un número.')
            continue  # Reinicia el ciclo del menú.
        else:
            try:
                # Estructura de control para ejecutar una acción según la opción seleccionada.
                match op:
                    case 1:
                        # Opción 1: Registrar un jugador en el equipo.
                        regP.regJugador(liga)
                    case 2:
                        # Opción 2: Mostrar la lista de jugadores del equipo.
                        regP.mostrarJ(liga)
                    case 3:
                        # Opción 3: Registrar el técnico del equipo.
                        regP.regTecnico(liga)
                    case 4:
                        # Opción 4: Registrar el asistente técnico.
                        regP.regAsisTecnico(liga)
                    case 5:
                        # Opción 5: Registrar el preparador físico.
                        regP.regPrepFisico(liga)
                    case 6:
                        # Opción 6: Registrar el cuerpo médico del equipo.
                        regP.regCuerpoMedico(liga)
                    case 7:
                        # Opción 7: Registrar estadísticas de un jugador.
                        regP.regEstadisticasJugador(liga)
                    case 8:
                        # Opción 8: Ver las estadísticas de un jugador.
                        regP.verEstadisticasJugador(liga)
                        clp.comandoPause()  # Pausa para que el usuario pueda ver las estadísticas.
                    case 9:
                        # Opción 9: Limpia la pantalla y sale del ciclo, terminando el registro de plantel.
                        clp.ejecutar_comandoLimp()
                        isAllow = False  # Cambia la variable de control para salir del ciclo.
                    case _:
                        # Si se ingresa una opción no válida, muestra un mensaje de error.
                        print('Opción ingresada no válida.')
                        clp.comandoPause()  # Pausa para que el usuario pueda leer el mensaje.
                        continue  # Reinicia el ciclo del menú.
            except Exception as e:
                # Si ocurre un error inesperado durante la ejecución, muestra un mensaje de error.
                print(f"Ha ocurrido un error: {e}")
                clp.comandoPause()  # Pausa la ejecución para que el usuario vea el mensaje.

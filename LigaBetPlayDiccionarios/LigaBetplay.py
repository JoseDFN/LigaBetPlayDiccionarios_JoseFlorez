"""
Programa que permite llevar el control y registro de los equipos, plantilla de jugadores, cuerpo técnico, y
estadísticas de los equipos. El programa permite:
1. Registrar equipos.
2. Registrar plantel o integrantes de los equipos (Jugadores, Técnico, Asistente técnico, Preparadores físicos y Cuerpo médico).
3. Obtener la siguiente información:
    a. Equipo que más goles ha marcado en el desarrollo del torneo.
    b. Equipo con más goles en contra.
    c. Equipo que ocupa el último puesto en la tabla de posiciones.
4. Registrar estadísticas por jugador (Goles anotados, tarjetas amarillas recibidas, tarjetas rojas recibidas, total de faltas cometidas).
    a. Mostrar estadísticas como: Jugador que más faltas ha cometido.
    b. Jugador que más tarjetas amarillas ha recibido.
5. Salir.
"""

# Importamos las librerías necesarias, que parecen ser módulos definidos en otros archivos.
from math import e  # Importa la constante 'e' de la librería math (parece no ser utilizada aquí).
import modules.limpiar as clp  # Módulo para limpiar la pantalla y pausar la ejecución.
import modules.Menus as msg  # Módulo que contiene los menús del programa.
import modules.Equipos as equipos  # Módulo que gestiona el registro y la información de los equipos.
import modules.regPlantel as regP  # Módulo para registrar el plantel de jugadores y cuerpo técnico.
import modules.programarPart as pPartido  # Módulo para programar partidos y gestionar estadísticas.
import modules.resultados as res  # Módulo para registrar y mostrar resultados.

# Función principal que ejecuta el programa.
if (__name__ == '__main__'):
    # Diccionario que almacena los equipos y partidos en la liga.
    liga = {
        'Equipos': {},  # Aquí se guardarán los equipos registrados.
        'Partidos': {}  # Aquí se guardarán los partidos jugados.
    }
    
    isLiga = True  # Variable de control para mantener el ciclo del programa en ejecución.
    
    # Bucle principal del programa.
    while isLiga:
        clp.ejecutar_comandoLimp()  # Limpia la pantalla.
        print(msg.MenuPrinPartes)  # Muestra el menú principal.
        
        try:
            op = int(input('Ingrese la opción: '))  # Captura la opción ingresada por el usuario.
        except ValueError:
            # En caso de que el usuario ingrese algo que no sea un número.
            print('Tipo de opción no válida. Por favor ingrese un número.')
            clp.comandoPause()  # Pausa la ejecución para que el usuario pueda leer el mensaje.
            continue  # Reinicia el ciclo.
        else:
            try:
                # Estructura de control para ejecutar una acción según la opción seleccionada.
                match op:
                    case 1:
                        equipos.regEquipos(liga)  # Llama a la función para registrar equipos.
                    case 2:
                        equipos.mEquipo(liga)  # Llama a la función para mostrar equipos.
                    case 3:
                        regP.regPlantel(liga)  # Llama a la función para registrar planteles (jugadores y cuerpo técnico).
                    case 4:
                        pPartido.addPartidos(liga)  # Llama a la función para programar partidos.
                    case 5:
                        pPartido.viewPartidos(liga)  # Llama a la función para mostrar los partidos programados.
                    case 6:
                        pPartido.regEstadisticasPartido(liga)  # Llama a la función para registrar estadísticas de los partidos.
                    case 7:
                        equipos.esEquipo(liga)  # Llama a la función para mostrar estadísticas por equipo.
                    case 8:
                        res.addResultados(liga)  # Llama a la función para registrar resultados de los partidos.
                    case 9:
                        res.tabla(liga)  # Llama a la función para mostrar la tabla de posiciones.
                    case 10:
                        clp.ejecutar_comandoLimp()  # Limpia la pantalla antes de salir.
                        isLiga = False  # Cambia la variable de control para salir del bucle y terminar el programa.
                    case _:
                        # Si la opción ingresada no es válida.
                        print('Opción ingresada no válida')
                        clp.comandoPause()  # Pausa para que el usuario pueda ver el mensaje.
                        continue  # Reinicia el ciclo.
            except Exception as e:
                # En caso de un error inesperado durante la ejecución del código.
                print(f"Ha ocurrido un error inesperado: {e}")
                clp.comandoPause()  # Pausa para que el usuario vea el mensaje antes de continuar.

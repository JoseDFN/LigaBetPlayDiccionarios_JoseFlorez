import os  # Módulo del sistema operativo (aunque no se utiliza explícitamente en este código).
import modules.programarPart as pa  # Módulo para gestionar partidos (visualización y programación).
import modules.limpiar as clp  # Módulo para limpiar la pantalla y pausar la ejecución.

def addResultados(liga):
    """Función para agregar los resultados de un partido"""
    
    clp.ejecutar_comandoLimp()  # Limpia la pantalla antes de mostrar el menú.
    
    print('Seleccione el partido para ingresar los resultados:')
    pa.viewPartidos(liga)  # Muestra los partidos disponibles para ingresar resultados.
    
    try:
        # Solicita al usuario ingresar el código del partido.
        codigoPartido = int(input('\nIngrese el código del partido al que desea ingresar resultados: '))
    except ValueError:
        # Si el usuario ingresa un valor no numérico, se muestra un mensaje de error.
        print("Código de partido no válido.")
        clp.comandoPause()  # Pausa la ejecución para que el usuario vea el mensaje.
        return  # Sale de la función.

    if codigoPartido not in liga['Partidos']:
        # Verifica si el código del partido existe en el diccionario 'Partidos'.
        print('El código del partido no existe.')
        clp.comandoPause()
        return

    # Recupera los detalles del partido seleccionado.
    partido = liga['Partidos'][codigoPartido]
    local = partido['local']  # Nombre del equipo local.
    visitante = partido['visitante']  # Nombre del equipo visitante.
    
    try:
        # Solicita al usuario ingresar los goles de ambos equipos.
        golesLocal = int(input(f'Ingrese los goles anotados por el equipo {local}: '))
        golesVisitante = int(input(f'Ingrese los goles anotados por el equipo {visitante}: '))
    except ValueError:
        # Si se ingresa un valor no numérico para los goles, se muestra un mensaje de error.
        print("Entrada de goles no válida, por favor ingrese un número.")
        clp.comandoPause()
        return
    
    # Guarda los resultados de goles en el diccionario del partido.
    partido['golesLocal'] = golesLocal
    partido['golesVisitante'] = golesVisitante
    print(f'El partido {local} vs {visitante} finalizó {golesLocal} - {golesVisitante}')

    # Busca los equipos correspondientes en el diccionario 'Equipos'.
    equipoLocal = next((equipo for equipo in liga['Equipos'].values() if equipo['nombreEqu'] == local), None)
    equipoVisitante = next((equipo for equipo in liga['Equipos'].values() if equipo['nombreEqu'] == visitante), None)

    if equipoLocal and equipoVisitante:
        # Si ambos equipos existen, se actualizan las estadísticas con los resultados del partido.
        actualizarEstadisticas(equipoLocal, equipoVisitante, golesLocal, golesVisitante)
    else:
        # Si no se encuentra alguno de los equipos, se muestra un mensaje de error.
        print("Uno de los equipos no existe en los registros.")
    
    clp.comandoPause()

def actualizarEstadisticas(equipoLocal, equipoVisitante, golesLocal, golesVisitante):
    """Actualiza las estadísticas de los equipos después de un partido"""
    
    # Actualiza las estadísticas para ambos equipos (local y visitante).
    for equipo, golesFavor, golesContra in [(equipoLocal, golesLocal, golesVisitante), (equipoVisitante, golesVisitante, golesLocal)]:
        estadisticas = equipo['estadisticas Equipo']  # Recupera el diccionario de estadísticas del equipo.
        estadisticas['partidosJugados'] += 1  # Incrementa el número de partidos jugados.
        estadisticas['golesaFavor'] += golesFavor  # Suma los goles a favor.
        estadisticas['golesenContra'] += golesContra  # Suma los goles en contra.

        if golesFavor > golesContra:
            # Si el equipo ganó, suma una victoria y 3 puntos.
            estadisticas['partidosGanados'] += 1
            estadisticas['totalPuntos'] += 3
        elif golesFavor < golesContra:
            # Si el equipo perdió, suma una derrota.
            estadisticas['partidosPerdidos'] += 1
        else:
            # Si el partido terminó en empate, suma un empate y 1 punto.
            estadisticas['partidosEmpatados'] += 1
            estadisticas['totalPuntos'] += 1

def tabla(liga):
    """Muestra la tabla de posiciones de la liga"""
    
    if not liga['Equipos']:
        # Si no hay equipos registrados, muestra un mensaje de advertencia.
        print("No hay equipos registrados en la liga.")
        clp.comandoPause()
        return

    clp.ejecutar_comandoLimp()  # Limpia la pantalla antes de mostrar la tabla.
    
    # Encabezado de la tabla de posiciones.
    print(f"{'Equipo':<20} {'PJ':<3} {'PG':<3} {'PP':<3} {'PE':<3} {'GF':<3} {'GC':<3} {'TP':<3}")
    print('-' * 50)
    
    # Ordena los equipos por puntos, y en caso de empate, por la diferencia de goles (GF - GC).
    equipos_ordenados = sorted(liga['Equipos'].values(), key=lambda x: (x['estadisticas Equipo']['totalPuntos'], x['estadisticas Equipo']['golesaFavor'] - x['estadisticas Equipo']['golesenContra']), reverse=True)
    
    # Muestra cada equipo con sus estadísticas en la tabla.
    for equipo in equipos_ordenados:
        nombreEquipo = equipo['nombreEqu']  # Nombre del equipo.
        estadisticas = equipo['estadisticas Equipo']  # Estadísticas del equipo.
        pj = estadisticas['partidosJugados']  # Partidos jugados.
        pg = estadisticas['partidosGanados']  # Partidos ganados.
        pp = estadisticas['partidosPerdidos']  # Partidos perdidos.
        pe = estadisticas['partidosEmpatados']  # Partidos empatados.
        gf = estadisticas['golesaFavor']  # Goles a favor.
        gc = estadisticas['golesenContra']  # Goles en contra.
        tp = estadisticas['totalPuntos']  # Total de puntos.
        
        # Formato de impresión de las estadísticas.
        print(f"{nombreEquipo:<20} {pj:<3} {pg:<3} {pp:<3} {pe:<3} {gf:<3} {gc:<3} {tp:<3}")
    
    clp.comandoPause()  # Pausa para que el usuario pueda ver la tabla.

from tablero import *

def obtener_movimientos_posibles(tablero, simbolo):
    movimientos = []
    i = 0
    while i < 8:
        j = 0
        while j < 8:
            if tablero[i][j] == simbolo:
                for di in [-1, 1]:
                    for dj in [-1, 1]:
                        ni = i + di
                        nj = j + dj
                        if 0 <= ni < 8 and 0 <= nj < 8:
                            if es_movimiento_valido(tablero, (i, j), (ni, nj), simbolo):
                                movimientos.append(((i, j), (ni, nj)))
                        ni2 = i + di * 2
                        nj2 = j + dj * 2
                        ni_m = i + di
                        nj_m = j + dj
                        if 0 <= ni2 < 8 and 0 <= nj2 < 8:
                            if 0 <= ni_m < 8 and 0 <= nj_m < 8:
                                if tablero[ni_m][nj_m] != " ":
                                    if es_movimiento_valido(tablero, (i, j), (ni2, nj2), simbolo):
                                        movimientos.append(((i, j), (ni2, nj2)))
            j += 1
        i += 1
    return movimientos


def evaluar_movimiento(tablero, origen, destino, simbolo, es_j1):
    fi, ci = origen
    ff, cf = destino
    puntaje = 0

    if es_j1:
        puntaje += fi - ff
    else:
        puntaje += ff - fi

    if abs(ff - fi) == 2:
        puntaje += 3

    return puntaje


def movimiento_computadora(tablero, simbolo, es_j1):
    movimientos = obtener_movimientos_posibles(tablero, simbolo)
    if len(movimientos) == 0:
        return None

    mejor = movimientos[0]
    mejor_puntaje = evaluar_movimiento(tablero, movimientos[0][0], movimientos[0][1], simbolo, es_j1)

    i = 1
    while i < len(movimientos):
        origen, destino = movimientos[i]
        puntaje = evaluar_movimiento(tablero, origen, destino, simbolo, es_j1)
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor = movimientos[i]
        i += 1

    return mejor



def pedir_movimiento_humano(tablero, nombre_jugador, nombre_comp, simbolo_humano):
    while True:
        limpiar_terminal()
        mostrar_tablero(tablero, nombre_jugador, nombre_comp)
        entrada = input(f"\n{nombre_jugador} ({simbolo_humano}) ? ").strip()

        if entrada == "-1":
            return "cancelar"

        coords = parsear_movimiento(entrada)
        if coords is None:
            print("Formato inválido. Usa formato como A8C6. Presiona Enter para continuar.")
            input()
            continue

        origen, destino = coords
        fi, ci = origen

        if tablero[fi][ci] != simbolo_humano:
            print("Esa casilla no tiene una pieza tuya. Presiona Enter para continuar.")
            input()
            continue

        if not es_movimiento_valido(tablero, origen, destino, simbolo_humano):
            print("Movimiento no válido. Presiona Enter para continuar.")
            input()
            continue

        return coords



def comenzar_jugador_vs_computadora(historial):
    limpiar_terminal()

    print("══════════════════════════════════════════")
    print("         JUGADOR VS COMPUTADORA           ")
    print("══════════════════════════════════════════")

    print("\n¿Cuál es tu nombre?")
    nombre_jugador = input("Ingrese su nombre: ").strip()
    while len(nombre_jugador) == 0:
        print("El nombre no puede estar vacío.")
        nombre_jugador = input("Ingrese su nombre: ").strip()

    nombre_comp = "Computadora"

    print(f"\n¿Quieres jugar primero? (S/N): ", end="")
    respuesta = input().strip().upper()
    while respuesta not in ["S", "N"]:
        print("Ingresa S o N: ", end="")
        respuesta = input().strip().upper()

    if respuesta == "S":
        nombre_j1    = nombre_jugador
        nombre_j2    = nombre_comp
        simbolo_hum  = "O"
        simbolo_comp = "X"
        comp_es_j1   = False
        turno        = 0 
    else:
        nombre_j1    = nombre_comp
        nombre_j2    = nombre_jugador
        simbolo_hum  = "X"
        simbolo_comp = "O"
        comp_es_j1   = True
        turno        = 0  

    tablero    = crear_tablero("O", "X")

    resultado = "Cancelado"

    while True:
        es_turno_comp = (turno == 0 and comp_es_j1) or (turno == 1 and not comp_es_j1)

        if es_turno_comp:
            limpiar_terminal()
            mostrar_tablero(tablero, nombre_j1, nombre_j2)
            print(f"\n{nombre_comp} ({simbolo_comp}) está pensando...")
            coords = movimiento_computadora(tablero, simbolo_comp, comp_es_j1)
            if coords is None:
                print("La computadora no tiene movimientos disponibles.")
                resultado = "Empate"
                break
            origen, destino = coords
            cols = "ABCDEFGH"
            fi, ci = origen
            ff, cf = destino
            print(f"{nombre_comp} ({simbolo_comp}) ? {cols[ci]}{8-fi}{cols[cf]}{8-ff}")
            mover_pieza(tablero, origen, destino)
            input("Presiona Enter para continuar...")
        else:
            coords = pedir_movimiento_humano(tablero, nombre_jugador, nombre_comp, simbolo_hum)
            if coords == "cancelar":
                limpiar_terminal()
                print("Juego cancelado.")
                resultado = "Cancelado"
                break
            origen, destino = coords
            mover_pieza(tablero, origen, destino)

        ganador_simbolo = hay_ganador(tablero, "O", "X")
        if ganador_simbolo is not None:
            if ganador_simbolo == simbolo_hum:
                nombre_ganador = nombre_jugador
            else:
                nombre_ganador = nombre_comp
            limpiar_terminal()
            mostrar_tablero(tablero, nombre_j1, nombre_j2)
            print(f"\n¡Ganador: {nombre_ganador}!")
            resultado = nombre_ganador
            break

        if turno == 0:
            turno = 1
        else:
            turno = 0

    registrar_partida(historial, nombre_j1, nombre_j2, resultado)
    input("\nPresiona Enter para volver al menú...")
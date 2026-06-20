from tablero import *
import time

def pedir_nombre():
    nombre = input("Ingrese su nombre: ").strip()
    if len(nombre) == 0:
        print("El nombre no puede estar vacío. Inténtalo de nuevo.")
        return pedir_nombre()
    for letra in nombre:
        if letra in "1234567890":
            print("El nombre no puede tener números. Inténtalo de nuevo.")
            return pedir_nombre()
        elif letra in "!@#$%^&*+()_+-¿?¡!-=~`[]{}|\\;:'\",.<>/?°":
            print("El nombre no puede tener caracteres especiales. Inténtalo de nuevo.")
            return pedir_nombre()
    return nombre


def mostrar_reglas():
    print("─" * 45)
    print("REGLAS DEL JUEGO:")
    print("1. Lleva todas tus piezas al lado opuesto.")
    print("2. Cada jugador tiene 8 piezas.")
    print("3. Las piezas se mueven en diagonal.")
    print("4. Puedes saltar sobre cualquier pieza si")
    print("   la casilla detrás está vacía.")
    print("5. No se capturan piezas del oponente.")
    print("6. Ingresa movimientos como: A8C6")
    print("   (columna+fila origen y columna+fila destino)")
    print("7. Escribe -1 para cancelar la partida.")
    print("─" * 45)


def pedir_movimiento(tablero, nombre_j1, nombre_j2, nombre_turno, simbolo):
    while True:
        limpiar_terminal()
        mostrar_tablero(tablero, nombre_j1, nombre_j2)
        entrada = input(f"\n{nombre_turno} ({simbolo}) ? ").strip()

        if entrada == "-1":
            return "cancelar"

        coords = parsear_movimiento(entrada)
        if coords is None:
            print("Formato inválido. Usa formato como A8C6. Presiona Enter para continuar.")
            input()
            continue

        origen, destino = coords
        fi, ci = origen


        if tablero[fi][ci] != simbolo:
            print("Esa casilla no tiene una pieza tuya. Presiona Enter para continuar.")
            input()
            continue

        if not es_movimiento_valido(tablero, origen, destino, simbolo):
            print("Movimiento no válido. Presiona Enter para continuar.")
            input()
            continue

        return coords


def comenzar_jugador_vs_jugador(historial):
    limpiar_terminal()

    print("══════════════════════════════════════════")
    print("         JUEGO ENTRE DOS JUGADORES        ")
    print("══════════════════════════════════════════")
    print(f"\n¿Cuál es el nombre del jugador 1, sera el (O)?")
    nombre_j1 = pedir_nombre()
    print(f"Jugador 1: {nombre_j1}  usara las fichas  O\n")

    print(f"¿Cuál es el nombre del jugador 2, sera el (X)?")
    nombre_j2 = pedir_nombre()
    print(f"Jugador 2: {nombre_j2}  usara las fichas  X\n")

    time.sleep(1)
    limpiar_terminal()


    mostrar_reglas()
    input("Presiona Enter para comenzar...")


    tablero   = crear_tablero("O", "X")

    turno = 0 

    resultado = "Cancelado"

    while True:
        if turno == 0:
            nombre_turno = nombre_j1
            simbolo      = "O"
        else:
            nombre_turno = nombre_j2
            simbolo      = "X"

        coords = pedir_movimiento(tablero, nombre_j1, nombre_j2, nombre_turno, simbolo)

        if coords == "cancelar":
            limpiar_terminal()
            print("Juego cancelado.")
            resultado = "Cancelado"
            break

        origen, destino = coords
        mover_pieza(tablero, origen, destino)

        ganador_simbolo = hay_ganador(tablero, "O", "X")
        if ganador_simbolo is not None:
            if ganador_simbolo == "O":
                nombre_ganador = nombre_j1
            else:
                nombre_ganador = nombre_j2
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
import os
def limpiar_terminal():
    print("\033[H\033[J", end="")


def crear_tablero(simbolo_j1, simbolo_j2):
    tablero = []
    for i in range(8):
        fila = []
        for j in range(8):
            fila.append(" ")
        tablero.append(fila)

    for i in range(6, 8):
        for j in range(8):
            if (i + j) % 2 == 0:
                tablero[i][j] = simbolo_j1

    for i in range(2):
        for j in range(8):
            if (i + j) % 2 == 0:
                tablero[i][j] = simbolo_j2

    return tablero


def crear_puntuacion(nombre_j1, nombre_j2):
    puntuacion = {nombre_j1: 0, nombre_j2: 0}
    return puntuacion


def actualizar_puntuacion(puntuacion, nombre_jugador):
    puntuacion[nombre_jugador] = puntuacion[nombre_jugador] + 1


def mostrar_tablero(tablero, puntuacion, nombre_j1, nombre_j2):
    print(f"  {nombre_j1}: {puntuacion[nombre_j1]} pts   |   {nombre_j2}: {puntuacion[nombre_j2]} pts")
    print()

    print("  A B C D E F G H")
    for i in range(8):
        fila_num = 8 - i
        print(f"{fila_num} ", end="")
        for j in range(8):
            celda = tablero[i][j]
            if celda == " ":
                print("_ ", end="")
            else:
                print(f"{celda} ", end="")
        print(f" {fila_num}")
    print("  A B C D E F G H")
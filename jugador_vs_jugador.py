from tablero import *

def pedir_nombre():
    nombre = input("Ingrese su nombre: ")
    for letra in nombre:
        if letra in "1234567890":
            print("El nombre no puede tener números. Vamos hacerlo denuevo.")
            return pedir_nombre()
        elif letra in "!@#$%^&*+()_+-¿?¡!-=~`[]{}|\\;:'\",.<>/?°¡!":
            print("El nombre no puede tener caracteres especiales. Vamos hacerlo denuevo.")
            return pedir_nombre()
    return nombre


def reglas_jugador_vs_jugador():
    print("Reglas del juego de damas:")
    print("1. El objetivo del juego es mover todas las piezas al lado contrario.")
    print("2. Cada jugador tiene 8 piezas.")
    print("3. Las piezas se mueven diagonalmente, una casilla a la vez.")
    print("4. Puedes saltar sobre cualquier pieza si la casilla detrás está vacía.")
    print("5. No se pueden capturar piezas del oponente.")
    print("6. Gana quien lleve todas sus piezas al lado opuesto.")


def comenzar_jugador_vs_jugador():
    nombre_jugadores = []
    limpiar_terminal()
    print("¡Hola!")
    for i in range(2):
        print(f"¿Cuál es el nombre del jugador {i + 1}?")
        nombre = pedir_nombre()
        nombre_jugadores.append(nombre)
        print(f"Jugador {i + 1}: {nombre}.")

    nombre_j1 = nombre_jugadores[0]
    nombre_j2 = nombre_jugadores[1]

    print()
    reglas_jugador_vs_jugador()
    print()

    tablero = crear_tablero("O", "X")
    puntuacion = crear_puntuacion(nombre_j1, nombre_j2)

    print(f"\nJuego {nombre_j1} vs {nombre_j2}")
    print()
    mostrar_tablero(tablero, puntuacion, nombre_j1, nombre_j2)

    return nombre_jugadores, tablero, puntuacion
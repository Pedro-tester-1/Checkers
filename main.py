from tablero import *
from jugador_vs_jugador import *
from jugador_vs_computadora import *
import pandas as pd
import os


def mostrar_menu():
    print("══════════════════════════════════════════")
    print("          JUEGO DAMAS CHINAS              ")
    print("══════════════════════════════════════════")
    print("  1. Jugardor vs Jugardor")
    print("  2. Jugardor vs Computadora")
    print("  3. Historial de partidas")
    print("  0. Salir")
    print("══════════════════════════════════════════")


def menu(historial):
    while True:
        limpiar_terminal()
        mostrar_menu()

        opcion = input("Opción: ").strip()

        if not opcion.isdigit():
            print("Opción inválida. Presiona Enter para continuar.")
            input()
            continue

        opcion = int(opcion)

        if opcion == 1:
            comenzar_jugador_vs_jugador(historial)

        elif opcion == 2:
            comenzar_jugador_vs_computadora(historial)

        elif opcion == 3:
            limpiar_terminal()
            mostrar_historial(historial)
            input("Presiona Enter para volver al menú...")

        elif opcion == 0:
            limpiar_terminal()
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Presiona Enter para continuar.")
            input()


if os.path.exists("historial.csv"):
    miDatos = pd.read_csv("historial.csv")
    historial = miDatos.to_dict(orient="records")
else:
    historial = []

menu(historial)
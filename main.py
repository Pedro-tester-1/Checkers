from jugador_vs_computadora import *
from jugador_vs_jugador import *
from tablero import *

def menu():
    print("Bienvenido al juego de damas.")
    modalidad = input("¿Desea jugar contra la computadora o contra otro jugador? (Escriba 'computadora' o 'jugador'): ")
    if modalidad == "computadora":
        print("Has elegido jugar contra la computadora.")
        comenzar_jugador_vs_computadora()
    elif modalidad == "jugador":
        print("Has elegido jugar contra otro jugador.")
        nombre_jugadores, tablero, puntuacion = comenzar_jugador_vs_jugador()
    else:
        limpiar_terminal()
        print("Opción no válida.")
        menu()




menu()

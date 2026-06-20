import os
from datetime import datetime
import pandas as pd


def limpiar_terminal():
    os.system("cls" if os.name == "nt" else "clear")



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


def mostrar_tablero(tablero, nombre_j1, nombre_j2):
    print(f"  {nombre_j1} (O)   vs   {nombre_j2} (X)")
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



def columna_a_indice(col):
    columnas = "ABCDEFGH"
    i = 0
    while i < len(columnas):
        if columnas[i] == col.upper():
            return i
        i += 1
    return -1


def fila_a_indice(fila):
    return 8 - fila


def parsear_movimiento(entrada):

    entrada = entrada.strip().upper()
    if len(entrada) != 4:
        return None
    col_i = columna_a_indice(entrada[0])
    col_f = columna_a_indice(entrada[2])
    if col_i == -1 or col_f == -1:
        return None
    if not entrada[1].isdigit() or not entrada[3].isdigit():
        return None
    fila_i = int(entrada[1])
    fila_f = int(entrada[3])
    if fila_i < 1 or fila_i > 8 or fila_f < 1 or fila_f > 8:
        return None
    return (fila_a_indice(fila_i), col_i), (fila_a_indice(fila_f), col_f)


def es_movimiento_valido(tablero, origen, destino, simbolo):

    fi, ci = origen
    ff, cf = destino

    if not (0 <= ff < 8 and 0 <= cf < 8):
        return False

    if tablero[ff][cf] != " ":
        return False

    dif_fila = ff - fi
    dif_col  = cf - ci

    if abs(dif_col) != abs(dif_fila):
        return False

    if abs(dif_fila) == 1:
        return True

    if abs(dif_fila) == 2:
        fila_media = fi + dif_fila // 2
        col_media  = ci + dif_col  // 2
        if tablero[fila_media][col_media] != " ":
            return True

    return False


def mover_pieza(tablero, origen, destino):
    """Mueve la pieza de origen a destino en el tablero."""
    fi, ci = origen
    ff, cf = destino
    tablero[ff][cf] = tablero[fi][ci]
    tablero[fi][ci] = " "


def contar_piezas_en_zona_victoria(tablero, simbolo, es_j1):
    contador = 0
    if es_j1:
        filas_victoria = [0, 1]
    else:
        filas_victoria = [6, 7]
    for i in filas_victoria:
        for j in range(8):
            if tablero[i][j] == simbolo:
                contador += 1
    return contador


def hay_ganador(tablero, simbolo_j1, simbolo_j2):
    if contar_piezas_en_zona_victoria(tablero, simbolo_j1, True) == 8:
        return simbolo_j1
    if contar_piezas_en_zona_victoria(tablero, simbolo_j2, False) == 8:
        return simbolo_j2
    return None


def registrar_partida(historial, nombre_j1, nombre_j2, resultado):
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    partida = {
        "jugadores": f"{nombre_j1} vs {nombre_j2}",
        "fecha_hora": fecha_hora,
        "resultado": resultado
    }
    historial.append(partida)
    
    # Guardar en CSV
    miDatos = pd.DataFrame(historial)
    miDatos.to_csv("historial.csv", index=False)


def mostrar_historial(historial):
    if len(historial) == 0:
        print("No hay juegos registrados aún.")
        return

    print()
    print("JUEGOS REALIZADOS")
    print("-" * 65)
    print("Num  Jugadores                 Fecha y Hora         Resultado")
    print("-" * 65)

    numero = 0
    while numero < len(historial):
        partida = historial[numero]
        print(f"{numero + 1}. {partida['jugadores']} | {partida['fecha_hora']} | {partida['resultado']}")
        numero += 1

    print()
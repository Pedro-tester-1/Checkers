def dibujar_tablero():
    print("  A B C D E F G H")
    for fila in range(8, 0, -1):
        print(f"{fila} ", end="")
        for col in range(8):
            if (fila + col) % 2 == 0:
                print("_ ", end="")
            else:
                print("  ", end="")
        print(f" {fila}")
    print("  A B C D E F G H")

dibujar_tablero()
def dibujar_tablero():
    print("  A B C D E F G H")
    for f in range(8, 0, -1):
        print(f"{f} ", end="")
        for c in range(8):
            if (f + c) % 2 == 0:
                print("_ ", end="")
            else:
                print("_ ", end="")
        print(f" {f}")
    print("  A B C D E F G H")

dibujar_tablero()

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

pedir_nombre()
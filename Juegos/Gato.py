import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def hay_ganador(tablero, jugador):
    # Comprobar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True

    # Comprobar columnas
    for columna in range(3):
        if all(tablero[fila][columna] == jugador for fila in range(3)):
            return True

    # Comprobar diagonales
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True

    return False

def tablero_lleno(tablero):
    return all(casilla != " " for fila in tablero for casilla in fila)

def gato():
    try:
        print("Bienvenido al juego del Gato (Tic-Tac-Toe)!")
        print("Cada casilla del tablero está representada por su posición del 1 al 9.")

        tablero = [[" " for _ in range(3)] for _ in range(3)]
        jugador_actual = "X"

        while True:
            imprimir_tablero(tablero)
            try:
                movimiento = int(input(f"{jugador_actual}, elige una casilla (1-9): "))

                if movimiento < 1 or movimiento > 9:
                    raise ValueError

                fila = (movimiento - 1) // 3
                columna = (movimiento - 1) % 3

                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador_actual

                    if hay_ganador(tablero, jugador_actual):
                        imprimir_tablero(tablero)
                        print(f"¡{jugador_actual} ha ganado!")
                        break

                    if tablero_lleno(tablero):
                        imprimir_tablero(tablero)
                        print("¡Empate!")
                        break

                    jugador_actual = "O" if jugador_actual == "X" else "X"
                else:
                    print("Casilla ocupada. Por favor, elige otra.")
            except ValueError:
                print("Opción inválida. Por favor, ingresa un número válido entre 1 y 9.")

    except KeyboardInterrupt:
        print("\nJuego interrumpido. ¡Hasta pronto!")

if __name__ == "__main__":
    gato()  # Ejecuta el juego del Gato al ejecutar este módulo directamente





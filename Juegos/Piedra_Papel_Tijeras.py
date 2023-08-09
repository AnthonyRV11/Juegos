import random

def OpcionJugador():
    # Permite al jugador elegir entre Piedra, Papel o Tijeras (p/r/t)
    while True:
        try:
            opcion_usuario = input("Elige Piedra, Papel o Tijeras (p/r/t): ").lower()
            if opcion_usuario in ['p', 'r', 't']:
                if opcion_usuario == 'p':
                    return "piedra"
                elif opcion_usuario == 'r':
                    return "papel"
                else:
                    return "tijeras"
            else:
                raise ValueError("Opción inválida. Por favor, elige 'p' para Piedra, 'r' para Papel o 't' para Tijeras.")
        except ValueError as error:
            print(error)

def OpcionComputadora():
    # Genera aleatoriamente la opción de la computadora entre Piedra, Papel o Tijeras
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

def Ganador(opcion_usuario, opcion_computadora):
    # Determina el ganador del juego comparando las opciones del jugador y la computadora
    if opcion_usuario == opcion_computadora:
        return "empate"
    elif (opcion_usuario == "piedra" and opcion_computadora == "tijeras") or \
         (opcion_usuario == "papel" and opcion_computadora == "piedra") or \
         (opcion_usuario == "tijeras" and opcion_computadora == "papel"):
        return "usuario"
    else:
        return "computadora"

def piedra_papel_tijeras():
    # Función principal que ejecuta el juego de Piedra, Papel o Tijeras
    print("Bienvenido a Piedra, Papel o Tijeras.")

    while True:
        try:
            jugador = OpcionJugador()  # El jugador elige su opción
            computadora = OpcionComputadora()  # La computadora elige aleatoriamente su opción

            print(f"Tú eliges: {jugador}")
            print(f"La computadora elige: {computadora}")

            ganador = Ganador(jugador, computadora)  # Determina el ganador del juego

            if ganador == "empate":
                print("Es un empate.")
            elif ganador == "usuario":
                print("Ganaste!")
            else:
                print("La computadora gana!")

            jugar_nuevamente = input("¿Quieres jugar de nuevo? (s/n): ").lower()
            if jugar_nuevamente != "s":
                break  # Si el jugador no quiere jugar nuevamente, sale del bucle y termina el juego
        except KeyboardInterrupt:
            print("\nJuego interrumpido. ¡Hasta pronto!")
            break
        except Exception as error:
            print(f"Ocurrió un error: {error}")

if __name__ == "__main__":
    piedra_papel_tijeras()  # Ejecuta el juego Piedra, Papel o Tijeras al ejecutar este módulo directamente

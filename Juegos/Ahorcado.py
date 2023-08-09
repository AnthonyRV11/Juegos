import random

def obtener_palabra():
    # Lista de palabras posibles para adivinar
    palabras = ["python", "desarrollo", "tecnologia", "computadora", "web", "analisis", "esfuerzo", "programacion", "avance", "developer"]
    return random.choice(palabras)  # Retorna una palabra aleatoria de la lista

def inicializar_palabra(palabra):
    # Crea una lista donde cada letra de la palabra se reemplaza por un guion bajo y los demás caracteres se mantienen igual
    return ["_" if letra.isalpha() else letra for letra in palabra]

def actualizar_palabra(palabra, letra, palabra_oculta):
    # Actualiza la palabra oculta reemplazando guiones bajos por la letra adivinada
    for i, letra_palabra in enumerate(palabra):
        if letra_palabra == letra:
            palabra_oculta[i] = letra

def dibujar_ahorcado(intentos):
    # Representaciones del ahorcado en diferentes estados
    ahorcado = [
        """
          +---+
          |   |
              |
              |
              |
              |
        =========
        """,
        # Se omiten los otros estados del ahorcado por brevedad...
        """
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        """
    ]
    return ahorcado[intentos]  # Retorna el dibujo correspondiente al número de intentos

def ahorcado():
    try:
        palabra = obtener_palabra()  # Obtiene una palabra aleatoria
        palabra_oculta = inicializar_palabra(palabra)  # Inicializa la palabra oculta con guiones bajos
        intentos = 0  # Inicializa el número de intentos
        letras_adivinadas = []  # Lista para almacenar las letras adivinadas

        print("---------------------------------------------------------------")
        print("Bienvenido al ahorcado!")
        print("Trata de adivinar las palabras en el menor número de intentos!")
        
        print("La palabra a adivinar: "," ".join(palabra_oculta))  # Muestra la palabra oculta al jugador
        print("---------------------------------------------------------------")

        while True:
            letra = input("Adivina una letra: ").lower()  # Solicita una letra al jugador y la convierte a minúsculas

            if letra in letras_adivinadas:
                print("Ya has adivinado esa letra. Intenta con otra.")
                continue  # Si la letra ya fue adivinada, pide otra letra nuevamente

            letras_adivinadas.append(letra)  # Agrega la letra adivinada a la lista de letras ya adivinadas

            if letra in palabra:
                actualizar_palabra(palabra, letra, palabra_oculta)  # Si la letra está en la palabra, actualiza la palabra oculta
            else:
                intentos += 1  # Si la letra no está en la palabra, incrementa el número de intentos
                print(dibujar_ahorcado(intentos))  # Muestra el dibujo correspondiente al ahorcado

            print("La palabra a adivinar: ", " ".join(palabra_oculta))  # Muestra la palabra oculta al jugador

            if "_" not in palabra_oculta:
                print("¡Felicidades! ¡Has adivinado la palabra!")
                break  # Si no quedan guiones bajos en la palabra oculta, muestra un mensaje de victoria y sale del bucle

            if intentos == len(dibujar_ahorcado(intentos)) - 1:
                print(f"Lo siento, has perdido. La palabra era '{palabra}'.")
                break  # Si se han agotado los intentos y el dibujo del ahorcado está completo, muestra un mensaje de derrota y sale del bucle
    except KeyboardInterrupt:
        print("\nJuego interrumpido. ¡Hasta pronto!")

if __name__ == "__main__":
    ahorcado()  # Ejecuta el juego del Ahorcado al ejecutar este módulo directamente

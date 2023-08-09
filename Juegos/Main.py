# Importando los módulos de los juegos
from Ahorcado import ahorcado
from Gato import gato
from Piedra_Papel_Tijeras import piedra_papel_tijeras

try:
    print("Bienvenido a mi juego!!!")

    while True:
        seleccion = int(input("Selecciona el número según lo que desees jugar: \n1. Ahorcado \n2. Gato \n3. Piedra, papel o tijeras \n4. Salir \n"))

        if seleccion == 1:
            ahorcado()  # Si se selecciona '1', ejecuta el juego del Ahorcado
        elif seleccion == 2:
            gato()  # Si se selecciona '2', ejecuta el juego del Gato (Tic-Tac-Toe)
        elif seleccion == 3:
            piedra_papel_tijeras()  # Si se selecciona '3', ejecuta el juego de Piedra, Papel o Tijeras
        elif seleccion == 4:
            print("Vuelve pronto!!!")  # Si se selecciona '4', muestra un mensaje de despedida
            break  # Sale del bucle y finaliza el programa
        else:
            print("Opción inválida. Por favor, selecciona un número válido.")

except ValueError:
    print("Opción inválida. Por favor, ingresa un número.")
except KeyboardInterrupt:
    print("\nSaliendo del programa. ¡Hasta pronto!")

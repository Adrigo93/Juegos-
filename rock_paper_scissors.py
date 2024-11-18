#piedra_papel_tijeras

import random

def piedra_papel_tijeras():
    opciones = ['piedra', 'papel', 'tijeras']
    print("Bienvenido al juego de Piedra, Papel o Tijeras")
    while True:
        jugador = input("Elige piedra, papel o tijeras (o 'salir' para terminar): ").lower()
        if jugador == 'salir':
            print("Gracias por jugar")
            break
        if jugador not in opciones:
            print("Opción no valida. Intentalo de nuevo.")
            continue
        ordenador = random.choice(opciones)
        print(f"El ordenador eligió: {ordenador}")

        if jugador == ordenador:
            print("Es un empate")
        elif(jugador == 'piedra' and ordenador == 'tijeras') or \
            (jugador == 'papel' and ordenador == 'piedra') or \
            (jugador == 'tijeras' and ordenador == 'papel'):
            print("Has ganado")
        else:
            print("El ordenador te gano, prueba de nuevo.")

        print()

if __name__ == "__main__":
    piedra_papel_tijeras()

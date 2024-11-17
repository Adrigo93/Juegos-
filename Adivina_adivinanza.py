##juego de adivinar

import ramdom

def adivina_el_numero():
    numero_secreto = ramdom.randint(1, 100)
    intentos = 0
    print("Bienvenido al juego de Adivina adivinanza")
    print("Estoy pensando un numero entre el 1 y 100.")

    while True:
        try:
            estimacion = int(input("Introduce tu estimaxion: "))
            intentos += 1

            if estimacion < numero_secreto:
                print("Muy bajo. Intenta de nuevo.")
            elif estimacion > numero_secreto:
            print("Muy alto. Intenta de nuevo.")
            else:
                print(f"Felicidades! Adivinaste el numero en {intentos} intentos.")
                break
        except ValueError:
            print("por favor, introduce un numero valido.")

if __name__ == "__main__":
    adivina_el_numero()

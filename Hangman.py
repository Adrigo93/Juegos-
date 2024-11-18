import random

def juego_ahorcado():
   
    palabras = ['españa', 'madrid', 'paris', 'arbol', 'oso', 'navidad', 'caracol', 'nieve']
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []  
    intentos = 6  

    print("Bienvenido al juego del Ahorcado en español")
    print("Adivina la palabra antes de que te quedes sin intentos")

    while intentos > 0:
        estado_palabra = ''
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                estado_palabra += letra  
            else:
                estado_palabra += '_'    
        print(f"\nPalabra: {estado_palabra}")
        print(f"Intentos restantes: {intentos}")

        
        if '_' not in estado_palabra:
            print(f"Felicidades, has adivinado la palabra secreta '{palabra_secreta}'.")
            break

        
        letra_usuario = input("Ingresa una letra: ").lower()

        
        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print("Por favor, ingresa solo una letra.")
            continue

        if letra_usuario in letras_adivinadas:
            print("Ya adivinaste esa letra, prueba otra distinta.")
            continue

        letras_adivinadas.append(letra_usuario)


        if letra_usuario in palabra_secreta:
            print("Genial,  has adivinado una letra de la palabra.")
        else:
            intentos -= 1
            print("La letra no esta en la palabra secreta.")

    else:
        
        print(f"\nLo siento, te has quedado sin intentos. La palabra era '{palabra_secreta}'.")

if __name__ == "__main__":
    juego_ahorcado()

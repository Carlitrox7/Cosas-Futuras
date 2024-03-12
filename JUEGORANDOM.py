import random

def adivina_el_numero():
    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número del 1 al 100. Tienes que adivinarlo en menos de 10 intentos.")

    numero_a_adivinar = random.randint(1, 100)
    intentos_restantes = 10

    while intentos_restantes > 0:
        intento = int(input("Introduce tu suposición: "))

        if intento < numero_a_adivinar:
            print("El número es mayor. Intenta de nuevo.")
        elif intento > numero_a_adivinar:
            print("El número es menor. Intenta de nuevo.")
        else:
            print("¡Felicidades! ¡Adivinaste el número!")
            break

        intentos_restantes -= 1
        print("Te quedan", intentos_restantes, "intentos.")

    if intentos_restantes == 0:
        print("Lo siento, has agotado todos tus intentos. El número era", numero_a_adivinar)

if __name__ == "__main__":
    adivina_el_numero()
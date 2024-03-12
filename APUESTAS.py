import random

def lanzar_moneda():
    # Generamos un número aleatorio entre 0 y 1
    resultado = random.randint(0, 1)
    # Si el resultado es 0, es cara; si es 1, es cruz
    return "cara" if resultado == 0 else "cruz"

def juego_de_apuestas(jugador1, jugador2, apuesta):
    # Realizamos el lanzamiento de la moneda
    resultado_lanzamiento = lanzar_moneda()
    
    # Comprobamos quién ganó la apuesta
    if resultado_lanzamiento == "cara":
        ganador = jugador1
    else:
        ganador = jugador2
    
    # El ganador recibe el doble de la apuesta
    ganador["dinero"] += apuesta * 2
    
    # Devolvemos el resultado del lanzamiento y el ganador
    return resultado_lanzamiento, ganador

# Función principal del juego
def main():
    print("¡Bienvenido al juego de apuestas de lanzamiento de monedas!")
    
    # Creamos dos jugadores
    jugador1 = {"nombre": input("Nombre del jugador 1: "), "dinero": 100}
    jugador2 = {"nombre": input("Nombre del jugador 2: "), "dinero": 100}
    
    # Loop principal del juego
    while True:
        print("\nDinero actual de", jugador1["nombre"], ":", jugador1["dinero"])
        print("Dinero actual de", jugador2["nombre"], ":", jugador2["dinero"])
        
        # Solicitamos la apuesta
        apuesta = int(input("\nIngrese la cantidad a apostar (0 para salir): "))
        if apuesta == 0:
            print("¡Gracias por jugar!")
            break
        
        # Validamos que los jugadores tengan suficiente dinero
        if apuesta > jugador1["dinero"] or apuesta > jugador2["dinero"]:
            print("Uno o ambos jugadores no tienen suficiente dinero para apostar esa cantidad.")
            continue
        
        # Realizamos el juego de apuestas
        resultado, ganador = juego_de_apuestas(jugador1, jugador2, apuesta)
        
        print("\n¡Resultado del lanzamiento de moneda:", resultado, "!")
        print("El ganador de la apuesta es:", ganador["nombre"])
        print("El nuevo saldo de", ganador["nombre"], "es:", ganador["dinero"])

# Ejecutamos el juego
if __name__ == "__main__":
    main()

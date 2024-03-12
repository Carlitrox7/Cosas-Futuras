def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(fila))
        print("-----")


def verificar_ganador(tablero):
    # Verificar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != ' ':
            return fila[0]

    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != ' ':
            return tablero[0][col]

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return tablero[0][2]

    return None


def jugar_gato():
    tablero = [[' ' for _ in range(3)] for _ in range(3)]
    jugador = 'X'

    while True:
        imprimir_tablero(tablero)
        fila = int(input(f"Jugador {jugador}, elige una fila (0, 1, 2): "))
        columna = int(input(f"Jugador {jugador}, elige una columna (0, 1, 2): "))

        if tablero[fila][columna] == ' ':
            tablero[fila][columna] = jugador
            ganador = verificar_ganador(tablero)
            if ganador:
                imprimir_tablero(tablero)
                print(f"¡El jugador {ganador} ha ganado!")
                break
            elif all(tablero[i][j] != ' ' for i in range(3) for j in range(3)):
                imprimir_tablero(tablero)
                print("¡Empate!")
                break
            jugador = 'O' if jugador == 'X' else 'X'
        else:
            print("Esa casilla ya está ocupada. Intenta de nuevo.")


if __name__ == "__main__":
    jugar_gato()
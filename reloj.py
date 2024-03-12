import time

def reloj():
    while True:
        # Obtenemos la hora actual
        hora_actual = time.localtime()
        
        # Formateamos la hora, minutos y segundos
        hora = hora_actual.tm_hour
        minutos = hora_actual.tm_min
        segundos = hora_actual.tm_sec
        
        # Imprimimos la hora en formato HH:MM:SS
        print(f"{hora:02}:{minutos:02}:{segundos:02}", end="\r")
        
        # Esperamos un segundo antes de actualizar la hora
        time.sleep(1)

# Ejecutamos el reloj
if __name__ == "__main__":
    reloj()

import numpy as np

cantidad_filas = 6
cantidad_columnas = 7

def crear_tablero():
    tablero = np.zeros((cantidad_filas, cantidad_columnas))
    return tablero

def soltar_pieza(tablero, fila, columna, pieza):
    tablero[fila][columna] =  pieza

def es_valido_lugar(tablero, columna):
    return tablero[cantidad_filas-1][columna] == 0

def abre_nueva_fila(tablero, columna):
    for fila in range(cantidad_filas):
        if tablero[fila][columna] == 0:
            return fila
        
def imprimir_tablero(tablero):
    print(np.flip(tablero, 0))

def movimiento_ganador(tablero, pieza):
    # revisar horizontales para ver ganador
    for col in range(cantidad_columnas-3):
        for fila in range(cantidad_filas):
            if tablero[fila][col] == pieza and tablero[fila][col+1] == pieza and tablero [fila][col+2] == pieza and tablero[fila][col+3] == pieza:
                return True
            
    # revisar verticales para ver ganador
    for col in range(cantidad_columnas):
        for fila in range(cantidad_filas-3):
            if tablero[fila][col] == pieza and tablero[fila+1][col] == pieza and tablero [fila+2][col] == pieza and tablero[fila+3][col] == pieza:
                return True
    
    # revisar diagonales positivas para ver ganador
    for col in range(cantidad_columnas-3):
        for fila in range(cantidad_filas-3):
            if tablero[fila][col] == pieza and tablero[fila+1][col+1] == pieza and tablero [fila+2][col+2] == pieza and tablero[fila+3][col+3] == pieza:
                return True
    
    # revisar diagonales negativas para ver ganador
    for col in range(cantidad_columnas-3):
        for fila in range(3, cantidad_filas):
            if tablero[fila][col] == pieza and tablero[fila-1][col+1] == pieza and tablero [fila-2][col+2] == pieza and tablero[fila-3][col+3] == pieza:
                return True                    


def dibujar_tablero(tablero):
    pass

tablero = crear_tablero()
imprimir_tablero(tablero)
juego_terminado = False
turno = 0

while not juego_terminado:
            
    if turno == 0:
        columna = int(input("Selecciona entre (0-6) jugador 1: "))
        
        if es_valido_lugar(tablero, columna):
            fila = abre_nueva_fila(tablero, columna)
            soltar_pieza(tablero, fila, columna, 1)
            
            if movimiento_ganador(tablero, 1):
                print("GANASTE JUGADOR 1!!")
                juego_terminado ==  True
                    
    else:
        columna = int(input("Selecciona entre (0-6) jugador 2: "))
        
        if es_valido_lugar(tablero, columna):
            fila = abre_nueva_fila(tablero, columna)
            soltar_pieza(tablero, fila, columna, 2)
            
            if movimiento_ganador(tablero, 2):
                print("GANASTE JUGADOR 2!!")
                juego_terminado ==  True
                
    
    imprimir_tablero(tablero)
    
    turno += 1
    turno = turno % 2
        
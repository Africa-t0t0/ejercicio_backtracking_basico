'''
    Ejercicio donde se debe recorrer una matriz por las casillas que estén disponibles.
    Los movimientos disponibles son arriba, abajo, izquierda y derecha.

    Asumo que siempre seran matrices de NxN
'''

MATRIZ = [
    [0,1,1,1,1,1],
    [0,1,0,0,0,1],
    [0,1,0,1,0,1],
    [0,0,0,1,0,1],
    [1,1,1,1,0,1],
    [1,1,1,1,0,0],
]

MATRIZ_2 = [
    [0,0,0,0,0,0],
    [1,1,1,1,1,0],
    [0,0,0,0,0,0],
    [0,1,1,1,1,1],
    [0,0,0,0,0,0],
    [1,1,1,1,1,0],
]

def subir(posicion_actual: list, matriz: list) -> list:
    eje_x = posicion_actual[0]
    eje_y = posicion_actual[1]
    if eje_x > 0:
        posicion_actual[0] = eje_x - 1
        return posicion_actual
    else:
        print(f'no se puede subir en la posicion ({eje_x},{eje_y})')
        return posicion_actual

def bajar(posicion_actual: list, matriz: list) -> list:
    eje_x = posicion_actual[0]
    eje_y = posicion_actual[1]
    largo_matriz = len(matriz)
    if eje_x < largo_matriz:
        posicion_actual[0] = eje_x + 1
        return posicion_actual
    else:
        print(f'no se puede subir en la posicion ({eje_x},{eje_y})')
        return posicion_actual

def izquierda(posicion_actual: list, matriz: list) -> list:
    eje_x = posicion_actual[0]
    eje_y = posicion_actual[1]
    largo_matriz = len(matriz)
    if eje_y > 0:
        posicion_actual[1] = eje_y - 1
        return posicion_actual
    else:
        print(f'no se puede subir en la posicion ({eje_x},{eje_y})')
        return posicion_actual

def derecha(posicion_actual: list, matriz: list) -> list:
    eje_x = posicion_actual[0]
    eje_y = posicion_actual[1]
    largo_matriz = len(matriz)
    if eje_y < largo_matriz:
        posicion_actual[1] = eje_y + 1
        return posicion_actual
    else:
        print(f'no se puede subir en la posicion ({eje_x},{eje_y})')
        return posicion_actual

def iniciar_recorrido(matriz: list, inicio: list, final: list) -> list:
    lista_puntos_visitados = []
    matriz_a_mostrar = matriz.copy()
    eje_x_inicio = inicio[0]
    eje_y_inicio = inicio[1]
    x_actual = eje_x_inicio
    y_actual = eje_y_inicio
    largo_matriz = len(matriz[0])
    while True:
        matriz_a_mostrar[x_actual][y_actual] = 'X'
        print(f'x: {x_actual} - y: {y_actual}')
        matriz_a_mostrar = matriz
        if [x_actual, y_actual] == [final[0] - 1, final[1] - 1]:
            break
        # Bajar
        if x_actual + 1 < largo_matriz and [x_actual + 1, y_actual] not in lista_puntos_visitados:
            if matriz[x_actual + 1][y_actual] == 0:
                x_actual = x_actual + 1
                lista_puntos_visitados.append([x_actual, y_actual])
                continue
            else:
                pass
        # Subir
        if x_actual - 1 < largo_matriz and [x_actual - 1, y_actual] not in lista_puntos_visitados:
            if matriz[x_actual - 1][y_actual] == 0:
                x_actual = x_actual - 1
                lista_puntos_visitados.append([x_actual, y_actual])
                continue
            else:
                pass

        # Derecha
        if y_actual + 1 < largo_matriz and [x_actual, y_actual + 1] not in lista_puntos_visitados:
            if matriz[x_actual][y_actual + 1] == 0:
                y_actual = y_actual + 1
                lista_puntos_visitados.append([x_actual, y_actual])
                continue
            else:
                pass

        # Izquierda
        if y_actual - 1 < largo_matriz and [x_actual, y_actual - 1] not in lista_puntos_visitados:
            if matriz[x_actual][y_actual - 1] == 0:
                y_actual = y_actual - 1
                lista_puntos_visitados.append([x_actual, y_actual])
                continue
            else:
                pass

    print(f'Finalizado, llegamos uwu \n {matriz}')


# iniciar_recorrido(matriz=MATRIZ, inicio=[0,0], final=[6,6])
iniciar_recorrido(matriz=MATRIZ_2, inicio=[0,0], final=[6,6])

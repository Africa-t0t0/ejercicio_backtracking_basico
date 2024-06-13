def iniciar_recorrido_back(matriz: list, punto_actual: list, final: list, lista_puntos_visitados: list):
    if punto_actual == [final[0]-1, final[1]-1]:
        print('Finalizado!!!')
        return

    x_actual, y_actual = punto_actual
    largo_matriz = len(matriz)
    print(f'X: {x_actual} - Y: {y_actual}')
    if x_actual + 1 < largo_matriz and [x_actual + 1, y_actual] not in lista_puntos_visitados:
        if matriz[x_actual + 1][y_actual] == 0:
            lista_puntos_visitados.append([x_actual + 1, y_actual])
            iniciar_recorrido_back(matriz, [x_actual + 1, y_actual], final, lista_puntos_visitados)
            return
    if x_actual - 1 < largo_matriz and [x_actual - 1, y_actual] not in lista_puntos_visitados:
        if matriz[x_actual - 1][y_actual] == 0:
            lista_puntos_visitados.append([x_actual - 1, y_actual])
            iniciar_recorrido_back(matriz, [x_actual - 1, y_actual], final, lista_puntos_visitados)
            return
    if y_actual + 1 < largo_matriz and [x_actual, y_actual + 1] not in lista_puntos_visitados:
        if matriz[x_actual][y_actual + 1] == 0:
            lista_puntos_visitados.append([x_actual, y_actual + 1])
            iniciar_recorrido_back(matriz, [x_actual, y_actual + 1], final, lista_puntos_visitados)
            return
    if y_actual - 1 < largo_matriz and [x_actual, y_actual - 1] not in lista_puntos_visitados:
        if matriz[x_actual][y_actual - 1] == 0:
            lista_puntos_visitados.append([x_actual, y_actual - 1])
            iniciar_recorrido_back(matriz, [x_actual, y_actual - 1], final, lista_puntos_visitados)
            return

    if [punto_actual[0], punto_actual[1]] == [x_actual, y_actual]:
        print('estamos atrapados!')
        punto_anterior = lista_puntos_visitados
        iniciar_recorrido_back(matriz, [punto_anterior[0], punto_anterior[1]], final, lista_puntos_visitados)
        return

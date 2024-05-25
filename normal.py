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
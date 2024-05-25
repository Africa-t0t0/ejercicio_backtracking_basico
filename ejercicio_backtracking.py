'''
    Ejercicio donde se debe recorrer una matriz por las casillas que estén disponibles.
    Los movimientos disponibles son arriba, abajo, izquierda y derecha.

    Asumo que siempre seran matrices de NxN
'''

from normal import *
from recursivo import *

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

MATRIZ_3 = [
    [0,0,1,0,0,0],
    [1,0,1,0,1,0],
    [0,0,1,0,1,0],
    [0,1,1,0,1,0],
    [0,0,0,0,1,0],
    [1,1,1,1,1,0]
]

MATRIZ_4 = [
    [0,0,0,0,0,0],
    [1,1,0,1,1,0],
    [1,1,0,1,1,0],
    [1,1,1,1,1,0],
    [1,1,1,1,1,0],
    [1,1,1,1,1,0]
]



# iniciar_recorrido(matriz=MATRIZ, inicio=[0,0], final=[6,6])
# iniciar_recorrido(matriz=MATRIZ_2, inicio=[0,0], final=[6,6])
# iniciar_recorrido_back(matriz=MATRIZ, punto_actual=[0,0], final=[6,6], lista_puntos_visitados=[])
# iniciar_recorrido_back(matriz=MATRIZ_2, punto_actual=[0,0], final=[6,6], lista_puntos_visitados=[])
iniciar_recorrido_back(matriz=MATRIZ_4, punto_actual=[0,0], final=[6,6], lista_puntos_visitados=[])

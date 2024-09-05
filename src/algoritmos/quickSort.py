import numpy as np
from src.utils.execution_time import measure_execution_time


@measure_execution_time
def quick_sort(array: np.array, p: int = 0, r: int = None):

    # tratamento caso o valor de r não for passado, como no caso da primeira chamada da funçao
    if r is None:
        r = len(array) - 1

    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)

    return np.array(array)


def partition(array: np.array, p: int, r: int):  # p = ponto de partida; r = right/direita

    pivot = array[r]
    i = p - 1

    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]  # swap

    array[i + 1], array[r] = array[r], array[i + 1]

    return i + 1

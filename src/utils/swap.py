import numpy as np


def swap(a, b, array: np.array):
    aux = array[a]
    array[a] = array[b]
    array[b] = aux

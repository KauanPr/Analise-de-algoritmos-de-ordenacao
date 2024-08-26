import numpy as np  # Biblioteca para trablahar com vetores
from src.utils.execution_time import measure_execution_time


@measure_execution_time # decorador para medir tempo
def bubble_sort(array: np.array):
    array = np.copy(array)
    #print(array)
    for i in range(len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j + 1], array[j]  # swap

    #print(array)
    return array


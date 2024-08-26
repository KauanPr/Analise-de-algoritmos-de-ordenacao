import numpy as np  # Biblioteca para trablahar com vetores
from src.utils.execution_time import measure_execution_time


@measure_execution_time  # decorador para medir tempo
def insertion_sort(array: np.array):

    array = np.copy(array)
    #print(array)

    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1

        array[j + 1] = key

    #print(array)
    return array



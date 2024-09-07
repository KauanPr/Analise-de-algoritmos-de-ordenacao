import numpy as np
from src.utils.execution_time import measure_execution_time


@measure_execution_time
def counting_sort(array: np.array):

    size = len(array)
    output = [0] * size
    k = max(array)

    # preencher o count
    count = [0] * (k + 1)
    for i in range(0, size):
        count[array[i]] += 1

    # Soma cumulativa
    for i in range(1, k + 1):
        count[i] += count[i - 1]


    # preencher o output
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    """    
    # passar copiar o output para o array
    for i in range(0, size):
        array[i] = output[i]
    """
    return np.array(output)

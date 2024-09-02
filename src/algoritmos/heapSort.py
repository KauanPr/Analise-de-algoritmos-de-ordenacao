import numpy as np  # Biblioteca para trablahar com vetores
from src.utils.execution_time import measure_execution_time
from src.utils.Heap import max_heapify

@measure_execution_time
def heap_sort(array: np.array):

    array = np.copy(array)
    size_heap = len(array)

    # contruir a max_heap
    for i in range(size_heap // 2, -1, -1):
        max_heapify(array, size_heap, i)

    for i in range(size_heap - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        max_heapify(array, i, 0)

    return np.array(array)







import numpy as np  # Biblioteca para trablahar com vetores
from src.utils import swap
from src.utils.execution_time import measure_execution_time


@measure_execution_time
def merge_sort(array: np.array):

    array = np.copy(array)

    if len(array) <= 1:
        return array

    center = len(array) // 2
    left_sub_array = array[:center]
    right_sub_array = array[center:]

    left_sub_array_sorted = merge_sort(left_sub_array)
    right_sub_array_sorted = merge_sort(right_sub_array)

    return merge(left_sub_array_sorted, right_sub_array_sorted)


def merge(left: np.array, right: np.array):
    final_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            final_array.append(left[i])
            i += 1
        else:
            final_array.append(right[j])
            j += 1

    # Quando um dos subvetores for lido por completo, descarrega o restante do outro subvetor no final do resultado
    final_array.extend(left[i:])
    final_array.extend(right[j:])

    return np.array(final_array)


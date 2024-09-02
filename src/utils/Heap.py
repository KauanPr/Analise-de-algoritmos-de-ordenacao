import numpy as np


def left(i: int):
    return 2 * i + 1

def right(i: int):
    return 2 * i + 2

def max_heapify(array: np.array, size_heap, i: int):
    l = left(i)
    r = right(i)
    largest = i

    if l < size_heap and array[i] < array[l]:
        largest = l

    if r < size_heap and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, size_heap, largest)



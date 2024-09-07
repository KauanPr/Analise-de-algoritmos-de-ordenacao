import numpy as np

from utils.use_cases import UseCases
from algoritmos import *

if __name__ == "__main__":
    #inc = int(input("inc: "))
    #fim = int(input("fim: "))
    #stp = int(input("stp: "))
    inc = 9999
    fim = 20000000
    stp = 100000000
    use_cases = UseCases(inc, fim, stp)
    test_array = use_cases.list_of_use_cases[0]['array']

    #bubble = bubble_sort(np.copy(test_array))
    #insert = insertion_sort(np.copy(test_array))
    merge = merge_sort(np.copy(test_array))
    heap = heap_sort(np.copy(test_array))
    quick = quick_sort(np.copy(test_array))
    counting = counting_sort(np.copy(test_array))
    print(counting[:5], counting[-5:])
    print(test_array[:5], test_array[-5:])

#
"""
TO DO:
 -  classe filha de UseCases para realizar a ordenação
"""

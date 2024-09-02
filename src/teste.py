from utils.use_cases import UseCases
from algoritmos import *
if __name__ == "__main__":
    #inc = int(input("inc: "))
    #fim = int(input("fim: "))
    #stp = int(input("stp: "))
    inc = 1000
    fim = 20000000
    stp = 100000000
    use_cases = UseCases(inc, fim, stp)


    bubble = bubble_sort(use_cases.list_of_use_cases[0]['array'])
    insert = insertion_sort(use_cases.list_of_use_cases[0]['array'])
    merge = merge_sort(use_cases.list_of_use_cases[0]['array'])
    heap = heap_sort(use_cases.list_of_use_cases[0]['array'])


#
"""
TO DO:
 -  classe filha de UseCases para realizar a ordenação
"""

import numpy as np
from src.algoritmos import *
from src.utils.use_cases import UseCases
from src.utils.sortValidator import is_sorted
import statistics


class apply_ordeinances:

    def __init__(self, use_cases):
        self.use_cases = use_cases

    def execute(self):
        for i in self.use_cases:
            print(i)
            self.apply_random_arrays(i)

    def apply_random_arrays(self, i):
        # Dicionario para armazenar arrays
        algorithms_time = {
            "bubble_sort": [],
            "insertion_sort": [],
            "merge_sort": [],
            "heap_sort": [],
            "quick_sort": [],
            "counting_sort": [],
        }
        for i_array, array in enumerate(self.use_cases[i]['random']['array']):
            ordered_arrays = []

            # Executar ordenações, e adicionar os arrays ordenados em uma lista para futura verificaçao
            ordered_arrays.append(bubble_sort(np.copy(array)))
            ordered_arrays.append(insertion_sort(np.copy(array)))
            ordered_arrays.append(merge_sort(np.copy(array)))
            ordered_arrays.append(heap_sort(np.copy(array)))
            ordered_arrays.append(quick_sort(np.copy(array)))
            ordered_arrays.append(counting_sort(np.copy(array)))

            # verificar se o array foi ordenado
            for array in ordered_arrays:
                if not is_sorted(array):
                    print("\nErro: vetor não foi ordenado\n")

            #
            algorithms_time['bubble_sort'].append(bubble_sort.execution_time[-1])
            algorithms_time['insertion_sort'].append(insertion_sort.execution_time[-1])
            algorithms_time['merge_sort'].append(merge_sort.execution_time[-1])
            algorithms_time['heap_sort'].append(heap_sort.execution_time[-1])
            algorithms_time['quick_sort'].append(quick_sort.execution_time[-1])
            algorithms_time['counting_sort'].append(counting_sort.execution_time[-1])

        # Fazer média do bubble
        self.use_cases[i]['random']['bubble_time'] = statistics.mean(algorithms_time['bubble_sort'])
        self.use_cases[i]['random']['insertion_time'] = statistics.mean(algorithms_time['insertion_sort'])
        self.use_cases[i]['random']['merge_time'] = statistics.mean(algorithms_time['merge_sort'])
        self.use_cases[i]['random']['heap_time'] = statistics.mean(algorithms_time['heap_sort'])
        self.use_cases[i]['random']['quick_time'] = statistics.mean(algorithms_time['quick_sort'])
        self.use_cases[i]['random']['counting_time'] = statistics.mean(algorithms_time['counting_sort'])


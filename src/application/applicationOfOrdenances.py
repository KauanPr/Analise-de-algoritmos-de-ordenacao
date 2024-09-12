import statistics

import numpy as np
from src.algoritmos import *
from src.utils.sortValidator import is_sorted


class apply_ordinances:

    def __init__(self, use_cases):
        self.use_cases = use_cases
        # Lista para executar as funções em loops para evitar blocos grandes de chamadas
        self.algorithms = ['bubble', 'insertion', 'merge', 'heap', 'quick', 'counting']
        self.funcions_algorithms = [bubble_sort, insertion_sort, merge_sort, heap_sort, quick_sort, counting_sort]
        self.types_array = ['random','reverse', 'sorted', 'nearly_sorted']

    def execute(self):
        for i in self.use_cases:
            print(i)
            self.apply_algorithms_in_arrays(i)

    def apply_algorithms_in_arrays(self, i):

        for type_array in self.types_array:
            print(f"************** {type_array.upper()} *****************")
            algorithms_time = {
                "bubble_sort": [],
                "insertion_sort": [],
                "merge_sort": [],
                "heap_sort": [],
                "quick_sort": [],
                "counting_sort": [],
            }

            for num, array in enumerate(self.use_cases[i][type_array]['array']):
                ordered_arrays = []
                print(f"----------Array - [{num + 1}] | Size arraya\: {i}:-----------")
                # Executar ordenações, e adicionar os arrays ordenados em uma lista para futura verificaçao
                for func in self.funcions_algorithms:
                    ordered_arrays.append(func(np.copy(array)))

                # verificar se o array foi ordenado
                for array_sorted in ordered_arrays:
                    if not is_sorted(array_sorted):
                        print("\nErro: vetor não foi ordenado\n")

                # adiciona os tempos de execução nos dicionarios
                for algorithm_name, func in zip(self.algorithms, self.funcions_algorithms):
                    algorithms_time[str(algorithm_name + '_sort')].append(func.execution_time[-1])

                #   realizar e armazenar a média de todos os algoritmos acima
                for algorithm_name in self.algorithms:
                    self.use_cases[i][type_array][str(algorithm_name + '_time')] = statistics.mean(
                        algorithms_time[str(algorithm_name + '_sort')])


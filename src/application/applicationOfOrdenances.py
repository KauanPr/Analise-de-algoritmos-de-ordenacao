import numpy as np
from src.algoritmos import *
from src.utils.use_cases import UseCases
from src.utils.sortValidator import is_sorted
import statistics


class apply_ordinances:

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

        # Lista para executar as funções em loops para evitar blocos grandes de chamadas
        algorithms = ['bubble', 'insertion', 'merge', 'heap', 'quick', 'counting']
        funcion_algorithms = [bubble_sort, insertion_sort, merge_sort, heap_sort, quick_sort, counting_sort]

        for i_array, array in enumerate(self.use_cases[i]['random']['array']):  # Percorrer a lista de arrays aleatorios
            ordered_arrays = []

            # Executar ordenações, e adicionar os arrays ordenados em uma lista para futura verificaçao
            for func in funcion_algorithms:
                ordered_arrays.append(func(np.copy(array)))

            # verificar se o array foi ordenado
            for array_sorted in ordered_arrays:
                if not is_sorted(array_sorted):
                    print("\nErro: vetor não foi ordenado\n")

            # adiciona os tempos de execução nos dicionarios
            for algorithm_name, func in zip(algorithms, funcion_algorithms):
                algorithms_time[str(algorithm_name + '_sort')].append(func.execution_time[-1])

        #   realizar e armazenar a média de todos os algoritmos acima
        for algorithm_name in algorithms:
            self.use_cases[i]['random'][str(algorithm_name + '_time')] = statistics.mean(algorithms_time[str(algorithm_name + '_sort')])

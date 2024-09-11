import random

import numpy as np
from typing import List, Dict, Any


class UseCases:

    def __init__(self, inc: int, fim: int, stp: int, rpt: int = 10):
        self.inc = inc
        self.fim = fim
        self.stp = stp
        self.rpt = rpt
        self.list_of_use_cases = dict() # local para guardar todos os casos de uso
        self.generate_use_cases()

    def generate_use_cases(self):

        for n in range(self.inc, self.fim + 1, self.stp): # "+ 1" para incluir o fim

            # array aleatorio
            random_lists = []
            for i in range(self.rpt):
                array = self.generate_random_array(n)
                random_lists.append(array)

            # array reverse
            reverse_arrays = [[]]
            for i in range(n):
                reverse_arrays[0].append(n - i)

            # Sorted array
            sorted_arrays = [[]]
            for i in range(n):
                sorted_arrays[0].append(i)

            # Nearly array
            nearly_arrays = []
            nearly_array = self.generate_random_array(n)    # gerar random array primeiro
            nearly_array.sort()                             # ordenar vetor
            amount_to_shuffle = int(n * 0.1)                # porçao qe vai ser embaralhada
            index_to_shuffle = random.sample(range(n), amount_to_shuffle)  # Seleciona 10% dos elementos

            shuffle_values = []                             # Separar os valores selecionados em um vetor
            for i in index_to_shuffle:
                shuffle_values.append(nearly_array[i])

            random.shuffle(shuffle_values)                  # Embalharar valores

            for i, index in enumerate(index_to_shuffle):       # Colocando os valores embaralhas de volta ao vetor
                nearly_array[index] = shuffle_values[i]
            nearly_arrays.append( nearly_array)

            # Colocando os arrays em um dicionario para facilitar o acesso
            use_cases = {
                "random": {'array': random_lists},
                "reverse": {'array': reverse_arrays},
                "sorted": {'array': sorted_arrays},
                "nearly_sorted": {'array': nearly_arrays}
            }
            self.list_of_use_cases[str(n)] = use_cases

    @staticmethod  # para poder testar ou gerar as arrays de forma direta
    def generate_random_array(size_array: int):

        max_value = size_array * 2

        # tratamento caso o max_value ultrapasse o valor maximo suportado por int32
        if max_value > 2147483647:
            max_value = 2147483647

        array = np.random.randint(size=size_array, low=0, high=max_value)
        return np.array(array)

    def show_use_cases(self):
        for i in self.list_of_use_cases:
            print(f"\nn: {i} | ")

            print("||RANDOM||")
            for j in self.list_of_use_cases[i]['random']:
                print(f"\t{j}")

            print("||REVERSE||")
            print(f"\t{self.list_of_use_cases[i]['reverse']}")

            print("||SORTED||")
            print(f"\t{self.list_of_use_cases[i]['sorted']}")

            print("||Nearly Sorted||")
            print(f"\t{self.list_of_use_cases[i]['nearly_sorted']}")



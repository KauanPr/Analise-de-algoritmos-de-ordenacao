import numpy as np
from typing import List, Dict, Any


class UseCases:

    def __init__(self, inc: int, fim: int, stp: int):
        self.inc = inc
        self.fim = fim
        self.stp = stp
        self.list_of_use_cases: List[Dict[str, Any]] = []  # local para guardar todos os casos de uso
        self.generate_use_cases()

    def generate_use_cases(self):
        for i in range(self.inc, self.fim, self.stp):
            array = self.generate_array(i)
            use_case = {
                "array": array,
                "n": i
            }
            self.list_of_use_cases.append(use_case)

    @staticmethod  # para poder testar ou gerar as arrays de forma direta
    def generate_array(size_array: int):

        max_value = size_array ** 2

        # tratamento caso o max_value ultrapasse o valor maximo suportado por int32
        if max_value > 2147483647:
            max_value = 2147483647


        array = np.random.randint(size=size_array, low=0, high=max_value)
        return array

    def show_use_cases(self):
        for i in self.list_of_use_cases:
            print(f"n: {i['n']} | array: {i['array']}")

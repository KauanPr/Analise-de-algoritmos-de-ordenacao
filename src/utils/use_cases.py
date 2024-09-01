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
    def generate_array(size_tam: int):
        array = np.random.randint(size=size_tam, low=0, high=size_tam ** 2)
        return array

    def show_use_cases(self):
        for i in self.list_of_use_cases:
            print(f"n: {i['n']} | array: {i['array']}")

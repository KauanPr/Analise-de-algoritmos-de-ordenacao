#   Kauan Cardoso Silva
#   Marco Antonio Menegati

import numpy as np

from utils.use_cases import UseCases
from application.applicationOfOrdenances import apply_ordeinances
from algoritmos import *

if __name__ == "__main__":
    #inc = int(input("inc: "))
    #fim = int(input("fim: "))
    #stp = int(input("stp: "))
    inc = 100
    fim = 100000
    stp = 10000000
    use_cases = UseCases(inc, fim, stp)
    use_cases.show_use_cases()
    print(use_cases.list_of_use_cases)
    app = apply_ordeinances(use_cases.list_of_use_cases)
    app.execute()
    print("teste de acesso a chave: " + str(use_cases.list_of_use_cases[str(inc)]['random']['bubble_time']))
    print('*' * 30)
    algorithms = ['bubble', 'insertion', 'merge', 'heap', 'quick', 'counting']
    #   realizar e armazenar a média de todos os algoritmos acima
    for algorithm in algorithms:
        print(f"{algorithm:10}:\t{use_cases.list_of_use_cases[str(inc)]['random'][str(algorithm + '_time')]:.6}")



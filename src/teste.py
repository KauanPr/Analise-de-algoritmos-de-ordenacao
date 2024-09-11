#   Kauan Cardoso Silva
#   Marco Antonio Menegati

import numpy as np
from utils.use_cases import UseCases
from utils.table_class import Table
from application.applicationOfOrdenances import apply_ordinances
from algoritmos import *
import sys


if __name__ == "__main__":

    #Aumente o limite de chamadas recursivas
    sys.setrecursionlimit(1000000)

    inc = 1000
    fim = 10000
    stp = 1000
    use_cases = UseCases(inc, fim, stp)
    #use_cases.show_use_cases()
    app = apply_ordinances(use_cases.list_of_use_cases)
    app.execute()
    print("teste de acesso a chave: " + str(use_cases.list_of_use_cases[str(inc)]['random']['bubble_time']))
    print('*' * 30)
    algorithms = ['bubble', 'insertion', 'merge', 'heap', 'quick', 'counting']
    #   realizar e armazenar a média de todos os algoritmos acima


    #print(f"dicio: {use_cases.list_of_use_cases}")
    tables = Table(use_cases.list_of_use_cases)
    tables.make_table()
    tables.print_table()



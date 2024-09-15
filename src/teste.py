# Autores:
#   Kauan Cardoso Silva
#   Marco Antonio Menegati


import sys

from application.applicationOfOrdenances import apply_ordinances
from utils.graph_creator import create_graph
from utils.table_class import Table
from utils.use_cases import UseCases

if __name__ == "__main__":

    # Aumente o limite de chamadas recursivas
    sys.setrecursionlimit(1000000)

    inc = 100
    fim = 500
    stp = 100
    use_cases = UseCases(inc, fim, stp)
    # use_cases.show_use_cases()
    app = apply_ordinances(use_cases.list_of_use_cases)
    app.execute()
    print("teste de acesso a chave: " + str(use_cases.list_of_use_cases[str(inc)]['random']['bubble_time']))
    print('*' * 30)

    table_names = ['random', 'reverse', 'sorted', 'nearly_sorted']
    #   realizar e armazenar a média de todos os algoritmos acima

    # print(f"dicio: {use_cases.list_of_use_cases}")
    tables = Table(use_cases.list_of_use_cases)
    tables.make_table()
    tables.print_table()

    tables_folder = str('../tables/' + str(inc) + '_' + str(fim))
    # salvamento das tabelas
    for table in tables.tables_names:
        tables.save_table_in_file(table, str(table + '_table.csv'), tables_folder)

    # Configurações de salvamento dos gráficos
    graphs_folder = str('../graphs/' + str(inc) + '_' + str(fim))

    faster_algs = ['merge', 'heap', 'quick', 'counting']
    slower_algs = ['bubble', 'insertion']

    # Criação das graficos
    for table_name in table_names:
        create_graph(table_instance=tables, table_name=table_name, graph_name=str(table_name + '_graph'),
                     folder_name=graphs_folder)
        create_graph(table_instance=tables, table_name=table_name, algorithms_in_graph=slower_algs,
                     graph_name=str(table_name + '_slower_graph'), folder_name=graphs_folder)
        create_graph(table_instance=tables, table_name=table_name, algorithms_in_graph=faster_algs,
                     graph_name=str(table_name + '_faster_graph'), folder_name=graphs_folder)

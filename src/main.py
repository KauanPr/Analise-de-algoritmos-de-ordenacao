#   Kauan Cardoso Silva
#   Marco Antonio Menegati

# Guia para execução:
# 1º - esteja localizado no diretório que *contenha* a pasta /src
# 2º - dê este comando no terminal (para que na compilação seja reconhicido a pasta src):
#      set PYTHONPATH=%cd%\src
# 3º - dê o comando para executar a main:
#      python -m src.main inc fim stp
#      (Opcional: se caso que queira alterar o numero de repetições, utilize: "--rpt valor_desejado")
# exemplo: python -m src.main 1000 10000 100 --rpt 15

import argparse
import sys

from .application.applicationOfOrdenances import apply_ordinances
from .utils.graph_creator import create_graph
from .utils.table_class import Table
from .utils.use_cases import UseCases


def main(inc: int = 1000, fim: int = 5000, stp: int = 200, rpt: int = 10, **kwargs):
    algorithms = ['bubble', 'insertion', 'merge', 'heap', 'quick', 'counting']
    table_names = ['random', 'reverse', 'sorted', 'nearly_sorted']

    # Aumente o limite de chamadas recursivas
    sys.setrecursionlimit(1000000)

    # Gerar casos de uso
    use_cases = UseCases(inc, fim, stp, rpt)

    # Aplicar ordenações
    app = apply_ordinances(use_cases.list_of_use_cases)
    app.execute()

    # Gerar tabelas
    tables = Table(use_cases.list_of_use_cases)
    tables.make_table()
    tables.print_table()

    # Salvar tabelas
    tables_folder = str('./tables/' + str(inc) + '_' + str(fim))
    for table in tables.tables_names:
        tables.save_table_in_file(table, str(table + '_table.csv'), tables_folder)

    # ---Gráficos---
    # Configurações de salvamento dos gráficos
    graphs_folder = str('./graphs/' + str(inc) + '_' + str(fim))

    # listas para gerar gráficos de algoritmos especificos
    # faster_algs = ['merge', 'heap', 'quick', 'counting']
    # slower_algs = ['bubble', 'insertion']
    slower_algs = algorithms[:2]
    faster_algs = algorithms[2:]

    # Criação das graficos
    for table_name in table_names:
        # Gerar com todos os algoritmos
        create_graph(table_instance=tables, table_name=table_name, graph_name=str(table_name + '_graph'),
                     folder_name=graphs_folder)
        # Gerar com os algoritmos mais lentos
        create_graph(table_instance=tables, table_name=table_name, algorithms_in_graph=slower_algs,
                     graph_name=str(table_name + '_slower_graph'), folder_name=graphs_folder)
        # Gerar com os algoritmos mais rápidos
        create_graph(table_instance=tables, table_name=table_name, algorithms_in_graph=faster_algs,
                     graph_name=str(table_name + '_faster_graph'), folder_name=graphs_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Passe valores para inc(inicio), fim, stp(step/intervalo) e rpt(repetições) (opcional).")

    # argumentos
    parser.add_argument('inc', type=int, help='Valor inicial (inc)')
    parser.add_argument('fim', type=int, help='Valor final (fim)')
    parser.add_argument('stp', type=int, help='Valor de passo (stp)')

    # argumentos opcionais
    parser.add_argument('--rpt', type=int, default=10, help='Repetições (rpt) - opcional, valor padrão é 10')

    # execução
    args = parser.parse_args()
    main(inc=args.inc, fim=args.fim, stp=args.stp, rpt=args.rpt)

import matplotlib.pyplot as plt
from .table_class import Table
import os


def create_graph(table_instance: Table, table_name: str, algorithms_in_graph: [] = None, graph_name: str = None,
                 folder_name: str = None):
    # obter a tabela passada nos parametros
    table = table_instance.tables[table_name]

    # Separar os dados da tabela
    n_values = [line[0] for line in table]  # Coluna de tamanhos de array 'n'

    bubble_sort_times = [line[1] for line in table]
    insertion_sort_times = [line[2] for line in table]
    merge_sort_times = [line[3] for line in table]
    heap_sort_times = [line[4] for line in table]
    quick_sort_times = [line[5] for line in table]
    counting_sort_times = [line[6] for line in table]

    sort_times = [bubble_sort_times, insertion_sort_times, merge_sort_times, heap_sort_times, quick_sort_times,
                  counting_sort_times]

    # Criando o gráfico
    plt.figure(figsize=(10, 6))

    # Plotar os tempos para cada algoritmo

    # Caso não seja definido quais algoritmos devem ser colocados no gráfico, todos os algoritmos serão colocados
    if algorithms_in_graph is None:
        algorithms_in_graph = ['bubble', 'insertion', 'merge', 'heap', 'quick', 'counting']

    for algorithm_time, algorithm in zip(sort_times, table_instance.algorithms_names):
        if algorithm in algorithms_in_graph:
            plt.plot(n_values, algorithm_time, label=str(algorithm + '_sort'), marker='o')

    # Configurações do gráfico
    plt.title(f'Tempo de execução dos algoritmos de ordenação || {table_name.upper()}')
    plt.xlabel('Tamanho do Array (n)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.legend(algorithms_in_graph)  # Exibe a legenda para identificar os algoritmos
    plt.grid(True)

    # Salvar o gráfico caso seja passado o local de salvemnto pelo parâmetro
    if graph_name is not None and folder_name is not None:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        address_file = os.path.join(folder_name, graph_name)
        plt.savefig(address_file)

    # Exibe o gráfico
    #plt.show()

    plt.close()

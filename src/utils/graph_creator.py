import matplotlib.pyplot as plt
from src.utils.table_class import Table

def create_graph(tables: Table, table_name: str):
    
    # obter a tabela passada nos parametros
    table = tables.tables[table_name]

    
    # Separar os dados da tabela
    n_values = [line[0] for line in table]  # Coluna de tamanhos de array 'n'
    
    # colocar os tempos em um dicionario
    algorithms_times = {
        "bubble_times": [],
        "insertion_times": [],
        "merge_times": [],
        "heap_times": [],
        "quick_times": [],
        "counting_times": []
    }

    bubble_sort_times = [line[1] for line in table]
    insertion_sort_times = [line[2] for line in table]
    merge_sort_times = [line[3] for line in table]
    heap_sort_times = [line[4] for line in table]
    quick_sort_times = [line[5] for line in table]
    counting_sort_times = [line[6] for line in table]

    # Criando o gráfico
    plt.figure(figsize=(10, 6))

    # Plotar os tempos para cada algoritmo
    plt.plot(n_values, bubble_sort_times, label='Bubble Sort', marker='o')
    plt.plot(n_values, insertion_sort_times, label='Insertion Sort', marker='o')
    plt.plot(n_values, merge_sort_times, label='Merge Sort', marker='o')
    plt.plot(n_values, heap_sort_times, label='Heap Sort', marker='o')
    plt.plot(n_values, quick_sort_times, label='Quick Sort', marker='o')
    plt.plot(n_values, counting_sort_times, label='Counting Sort', marker='o')

    # Configurações do gráfico
    plt.title(f'Tempo de execução dos algoritmos de ordenação || {table_name.upper()}')
    plt.xlabel('Tamanho do Array (n)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.legend()  # Exibe a legenda para identificar os algoritmos
    plt.grid(True)

    # Exibe o gráfico
    plt.show()


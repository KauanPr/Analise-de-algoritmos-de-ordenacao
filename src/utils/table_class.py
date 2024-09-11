

class Table:

    def __init__(self, list_use_cases):
        self.use_cases = list_use_cases
        self.tables = {
            'random': [],
            'reverse': [],
            'sorted': [],
            'nearly_sorted': []
        }
        self.tables_names = ['random', 'reverse', 'sorted', 'nearly_sorted']
        self.algorithms_names = ['bubble', 'insertion', 'merge', 'heap', 'quick', 'counting']

    def make_table(self):

        for table in self.tables_names:
            for n in self.use_cases:
                array_times = [int(n)]
                for algorithm in self.algorithms_names:
                    array_times.append(float(self.use_cases[n][table][str(algorithm + '_time')]))

                self.tables[table].append(array_times)

    def print_table(self):
        pre = 15        # espaçamento antes de imprimir
        pos = 8         # espaçamento após imprimir
        n_spacing = 8
        for table in self.tables_names:
            #   Titulo
            print(f"\n||{str(table).upper()}||")

            #   Cabeçalho
            header_line = f"{'n':>{n_spacing}}\t"
            for algorithm in self.algorithms_names:
                header_line += f'{algorithm:>{pre}}\t'
            print(header_line)

            # calcular o tamnho da linha de "----------"                   v valor para compensar os \t
            print(f"-" * (n_spacing + (pre * len(self.algorithms_names)) + 9))

            #   Linhas
            for line in self.tables[table]:
                #   Formatação da linha
                line_print = ""
                for item in line:
                    if isinstance(item, int):
                        line_print += f"{item:>{n_spacing}}\t"
                    elif isinstance(item, float):
                        line_print += f"{item:{pre}.{pos}f}\t"
                print(line_print)

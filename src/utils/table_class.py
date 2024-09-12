import os


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

        # atributos para formatação
        self.pre = 15  # espaçamento antes de imprimir
        self.pos = 8  # espaçamento após imprimir
        self.n_spacing = 8

    def make_table(self):

        for table in self.tables_names:
            for n in self.use_cases:
                array_times = [int(n)]
                for algorithm in self.algorithms_names:
                    array_times.append(float(self.use_cases[n][table][str(algorithm + '_time')]))

                self.tables[table].append(array_times)

    def print_table(self):
        for table in self.tables_names:
            #   Titulo
            print(f"\n||{str(table).upper()}||")

            #   Cabeçalho
            header_line = f"{'n':>{self.n_spacing}}\t"
            for algorithm in self.algorithms_names:
                header_line += f'{algorithm:>{self.pre}}\t'
            print(header_line)

            # calcular o tamnho da linha de "----------"                   v valor para compensar os \t
            print(f"-" * (self.n_spacing + (self.pre * len(self.algorithms_names)) + 9))

            #   Linhas
            for line in self.tables[table]:
                #   Formatação da linha
                line_print = self.format_line(line)
                print(line_print)

    import os

    def save_table_in_file(self, type_array: str, file_name: str, dir_adress: str):
        # Verifica se o diretório existe, se não existir, cria o diretório
        if not os.path.exists(dir_adress):
            os.makedirs(dir_adress)

            # Cria o arquivo e escreve no arquivo
        with open(os.path.join(dir_adress, file_name), 'w') as file:
            file.write(f"||{type_array.upper()}||\n")

            header_line = f"{'n':>{self.pre}}"
            for algorithm in self.algorithms_names:
                header_line += f'{algorithm:>{self.pre}}'
            file.write(header_line + "\n")

            for line in self.tables[type_array]:
                line_print = self.format_line(line)
                file.write(line_print + "\n")

    def format_line(self, line):
        line_print = ""
        for item in line:
            if isinstance(item, int):
                line_print += f"{item:>{self.n_spacing}}\t"
            elif isinstance(item, float):
                line_print += f"{item:{self.pre}.{self.pos}f}\t"

        return line_print

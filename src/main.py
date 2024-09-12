#   Kauan Cardoso Silva
#   Marco Antonio Menegati
import sys
import argparse
from utils.use_cases import UseCases
from utils.table_class import Table
from application.applicationOfOrdenances import apply_ordinances


def main(inc: int = 1000,fim: int = 5000 , stp: int= 200, rpt: int = 10, **kwargs):

    #Aumente o limite de chamadas recursivas
    sys.setrecursionlimit(1000000)

    use_cases = UseCases(inc, fim, stp, rpt)

    app = apply_ordinances(use_cases.list_of_use_cases)
    app.execute()

    tables = Table(use_cases.list_of_use_cases)
    tables.make_table()
    tables.print_table()



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Passe valores para inc(inicio), fim, stp(step/intervalo) e rpt(repetições) (opcional).")

    #argumentos
    parser.add_argument('inc', type=int, help='Valor inicial (inc)')
    parser.add_argument('fim', type=int, help='Valor final (fim)')
    parser.add_argument('stp', type=int, help='Valor de passo (stp)')

    # argumentos opcionais
    parser.add_argument('--rpt', type=int, default=1, help='Repetições (rpt) - opcional, valor padrão é 1')

    # execução
    args = parser.parse_args()
    main(inc=args.inc, fim=args.fim, stp=args.stp, rpt=args.rpt)
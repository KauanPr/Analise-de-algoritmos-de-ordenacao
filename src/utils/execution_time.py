import time
from functools import wraps

def measure_execution_time(function):
    @wraps(function)                # Decorador que envolve a função
    def wrapper(*args, **kwargs):

        # is_running implentado para corrigir problema ao medir tempo de funções recursivas
        if not hasattr(wrapper, 'is_running'): # verifica se a função já está em execução
            wrapper.is_running = False

        if not wrapper.is_running:
            wrapper.is_running = True
            init_time = time.time()     # Marca o tempo de inicio
            try:
                result = function(*args, **kwargs) # starta a função

            finally:
                end_time = time.time()      # Marca o tempo de termino

                if not hasattr(wrapper, 'times'): # se a função do decorador não tiver uma lista de execuções, uma nova é criada
                    wrapper.execution_time = []

                wrapper.execution_time.append(end_time - init_time)  #armazerna o tempo de execução, podendo ser acessado por "funcao".execution_time
                #print(f'Tempo de execução de {function.__name__}: {wrapper.execution_time[-1]:.6} segundos')
                wrapper.is_running = False                           # quando função se encerrar, definir como o is_running como False
        else:
            result = function(*args, **kwargs) # executa as funçoes chamadas pela recursao sem medir o tempo
        return result
    return wrapper



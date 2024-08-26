import time
from functools import wraps

def measure_execution_time(function):
    @wraps(function)                # Decorador que envolve a função
    def wrapper(*args, **kwargs):
        init_time = time.time()     # Marca o tempo de inicio
        result = function(*args, **kwargs) # starta a função
        end_time = time.time()      # Marca o tempo de termino

        wrapper.execution_time = end_time - init_time  #armazerna o tempo de execução, podendo ser acessado por "funcao".execution_time
        print(f'Tempo de execução de {function.__name__}: {wrapper.execution_time:.6} segundos')
        return result

    wrapper.execution_time = None # zera o tempo de execução
    return wrapper



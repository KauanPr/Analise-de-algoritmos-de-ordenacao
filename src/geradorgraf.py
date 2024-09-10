import matplotlib.pyplot as plt

def gerar_grafico(y1,y2,y3, x):
    algoritmos = ['Algoritmo 1', 'Algoritmo 2', 'Algoritmo 3', 'Algoritmo 4', 'Algoritmo 5', 'Algoritmo 6']
    
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3,)
    plt.xlabel('n(Quantidade de Números em um Conjunto A)')
    plt.ylabel('Tempo de Execução (segundos)')
    plt.title('Algoritmos de Ordenação')
    plt.legend(algoritmos)
    plt.grid(True)
    plt.show()

# Exemplo de uso
tempo_execucao1 = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
tempo_execucao2 = [0, 0.2, 0.4, 0.6, 0.8, 1, 1.2]
tempo_execucao3 = [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9]
#Utilizar o valor mínimo de tempo para ser o primeiro 
#após zero e o valor máximo como teto, depois disso,
#dividir esse intervalo por 4, para ter 6 eixos y, além de zero.
n = [0, 2000, 4000, 6000, 8000, 10000, 12000]

gerar_grafico(tempo_execucao1, tempo_execucao2, tempo_execucao3, n)
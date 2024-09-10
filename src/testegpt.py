import matplotlib.pyplot as plt

# Mais valores em x do que em y
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 3, 5]  # Menos valores

# Repetindo ou estendendo os valores de y para combinar com x
y_repetido = y * (len(x) // len(y)) + y[:len(x) % len(y)]

# Plotando
plt.plot(x, y_repetido, label='Y repetido')

# Adicionando título e rótulos
plt.title('Gráfico com mais valores em X do que em Y')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibindo a legenda
plt.legend()

# Exibindo o gráfico
plt.show()

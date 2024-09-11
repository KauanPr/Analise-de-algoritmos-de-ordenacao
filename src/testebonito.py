import matplotlib.pyplot as plt

# Create some data to plot
x = [0, 2000, 4000, 6000, 8000, 10000]
y1 = [0, 3.64, 9.46, 16.95, 37.14, 68.22]
y2 = [0, 22.05, 22.49, 30.65, 53.58, 47.33]
y3 = [0, 16.82, 26.10, 49.61, 47.59, 95.82]
y = [y1, y2, y3]  # Store each series of the data in one list

labels = ["Algoritmo A", "Algoritmo B", "Algoritmo C"]

fig, ax = plt.subplots(
    figsize=(6, 5)
)  # This sets the figure size to 6 inches wide by 5 inches high

# Plot the three model lines
for i, label in enumerate(labels):
    ax.plot(x, y[i], label=label)

ax.set_xlabel("n(Quantidade de Números em um Conjunto A)'")
ax.set_ylabel("Tempo de Execução (segundos)")
ax.legend()
ax.grid(True)
plt.show()
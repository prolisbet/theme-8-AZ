import matplotlib.pyplot as plt

x = [1, 4, 6, 7]
y = [3, 5, 8, 10]

plt.scatter(x, y)

plt.title('Диаграмма рассеивания')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()
plt.axhline(max(y))
plt.axvline(max(x))

plt.show()

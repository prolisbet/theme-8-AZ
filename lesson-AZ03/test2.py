import matplotlib.pyplot as plt

data = [5, 6, 7, 4, 6, 5, 7, 8, 9, 10, 11, 8, 9, 10, 7, 6, 5, 8]

plt.hist(data, bins=3)

plt.title('Кол-во часов сна')
plt.xlabel('Часы сна')
plt.ylabel('Кол-во людей')

plt.show()
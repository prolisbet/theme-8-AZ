import numpy as np
import matplotlib.pyplot as plt

array1 = np.random.rand(10)
array2 = np.random.rand(10)

plt.scatter(array1, array2, color='green')

plt.title('Диаграмма рассеяиния наборов случайных чисел')
plt.xlabel('Набор 1')
plt.ylabel('Набор 2')

for i in range(10):
    vline = array1[i]
    xline = array2[i]
    plt.axvline(vline, color='green', linewidth=0.2)
    plt.axhline(xline, color='green', linewidth=0.2)

plt.show()

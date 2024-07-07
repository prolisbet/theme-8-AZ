import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)

y = x ** 2

plt.plot(x, y)

plt.title('График функции y = x**2')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid()
plt.axhline(max(y), color='red')

plt.show()

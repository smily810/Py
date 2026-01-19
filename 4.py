#4a
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 2, 1]
plt.bar(x, y, color='green')
plt.title('Bar Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

#4b
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

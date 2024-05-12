import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lineplot using Sin and Cosine
x1 = np.linspace(0, 10, 100)
fig = plt.figure()
plt.plot(x1, np.sin(x1), '-')
plt.plot(x1, np.cos(x1), '--')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine and Cosine Functions')
plt.legend(['Sine', 'Cosine'])
plt.show()
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

# Lineplot
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()

# Scatter Plot
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)
plt.scatter(x_scatter, y_scatter)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.show()

# Histogram
data1 = np.random.randn(1000)
plt.hist(data1)
plt.show()

# Barplot
data2 = [5. , 25. , 50. , 20.]
plt.bar(range(len(data2)), data2)
plt.show()

# Piechart
plt.figure(figsize=(7,7))
x10 = [35, 25, 20, 20]
labels = ['Computer', 'Electronics', 'Mechanical', 'Chemical']
plt.pie(x10, labels=labels)
plt.show()

# Boxplot
data3 = np.random.randn(100)
plt.boxplot(data3)
plt.show()

# Grid
x15 = np.arange(1, 5)
plt.plot(x15, x15*1.5, x15, x15*3.0, x15, x15/3.0)
plt.grid(True)
plt.show()

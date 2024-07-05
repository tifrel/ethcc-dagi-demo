import numpy as np
import matplotlib.pyplot as plt

# formula: y = 3x + 1

x = np.random.normal(0, 1, 10)
noise = np.random.uniform(0, 1, 10)
y = 3 * x + 1 + noise

data = np.column_stack((x, y))
print(data)

np.savetxt('initial.csv', data[:5], delimiter=',', header='x,y', comments='', fmt='%.6f')
np.savetxt('contributions.csv', data[5:], delimiter=',', header='x,y', comments='', fmt='%.6f')

# Create a plot
plt.figure()
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = 3x + 1')
plt.legend()

# Save the plot as a PNG file
plt.savefig('plot.png')
plt.close()

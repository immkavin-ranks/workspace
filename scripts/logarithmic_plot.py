import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(0, 4 * np.pi, 400)  # 400 points between 0 and 4*pi

# Define the function y = 1.1 + sin(x)
y = 1.1 + np.sin(x)

# Create the logarithmic y-scale plot
plt.semilogy(x, y)

# Set axis labels and a title
plt.xlabel('x')
plt.ylabel('log(y)')
plt.title('Plot of y = 1.1 + sin(x) with Logarithmic Y Scale')

# Show the plot
plt.grid(True)
plt.show()

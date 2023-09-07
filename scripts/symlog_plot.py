import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.linspace(0, 4 * np.pi, 400)  # 400 points between 0 and 4*pi

# Define the function y = sin(x)
y = np.sin(x)

# Create the plot with symlog y-scale and set linear interval
plt.semilogy(x, y, basex=10, linthreshy=0.1)

# Set the y-axis limits to the linear interval
plt.ylim(-0.1, 0.1)

# Set axis labels and a title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = sin(x) with Symlog Y Scale (Linear Interval: -0.1 to 0.1)')

# Show the plot
plt.grid(True)
plt.show()

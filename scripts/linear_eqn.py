import numpy as np

# Coefficients of the linear equations
coefficients = np.array([[1, 3, -2],
                         [3, 5, 6],
                         [2, 4, 3]])

# Constants on the right-hand side of the equations
constants = np.array([5, 7, 8])

# Solve the system of equations
solution = np.linalg.solve(coefficients, constants)

# Extract the solution values
x1, x2, x3 = solution

print("Solution:")
print(f"x1 = {x1:.2f}")
print(f"x2 = {x2:.2f}")
print(f"x3 = {x3:.2f}")

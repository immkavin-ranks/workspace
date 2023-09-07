import numpy as np
from sympy import symbols, Eq, solve

# Define the variable
x = symbols('x')

# Define the quartic equation
equation = Eq(x**4 - 8*x**3 + 17*x**2 + 22*x - 104, 0)

# Find the roots symbolically
symbolic_roots = solve(equation, x)

print("Roots:")
for i, root in enumerate(symbolic_roots):
    print(f"Root {i + 1}: {root}")

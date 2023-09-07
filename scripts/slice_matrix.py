import numpy as np

# Create the matrix
matrix = np.array([[3.5, 6, 7],
                   [6, 4.5, 8],
                   [7, 8, 5.5]])

# Slice out the second column
second_column = matrix[:, 1]

# Slice out the last row
last_row = matrix[-1, :]

print("Original Matrix:")
print(matrix)

print("\nSecond Column:")
print(second_column)

print("\nLast Row:")
print(last_row)

import sys

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print("Usage: python factorial.py <integer>")
    sys.exit(1)

# Get the integer from the command-line argument
try:
    num = int(sys.argv[1])
except ValueError:
    print("Error: Please provide a valid integer.")
    sys.exit(1)

# Check if the number is non-negative
if num < 0:
    print("Error: Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")

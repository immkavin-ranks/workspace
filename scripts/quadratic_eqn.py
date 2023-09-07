import math

# Coefficients of the quadratic equation
a = 2
b = -17
c = 35

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
    # Two real and distinct solutions
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two real and distinct solutions:")
    print("x1 =", x1)
    print("x2 =", x2)
elif discriminant == 0:
    # One real solution (double root)
    x1 = -b / (2*a)
    print("One real solution (double root):")
    print("x =", x1)
else:
    # Complex solutions
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print("Complex solutions:")
    print("x1 =", real_part, "+", imaginary_part, "i")
    print("x2 =", real_part, "-", imaginary_part, "i")

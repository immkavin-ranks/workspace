import math

# Define the range of integers
start = 0
end = 20

# Define the number of decimal places for square and cube roots
decimal_places = 2

# Create and open a file for writing
with open("roots.txt", "w") as file:
    # Write the header
    file.write("Number\tSquare Root\tCube Root\n")
    
    # Generate and write the data to the file
    for num in range(start, end + 1):
        square_root = round(math.sqrt(num), decimal_places)
        cube_root = round(num ** (1/3), decimal_places)
        file.write(f"{num}\t{square_root}\t{cube_root}\n")

print("Data has been written to 'roots.txt' file.")

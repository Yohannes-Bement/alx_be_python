# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a variable for row count
row = 0

# Use a while loop to handle the rows of the pattern
while row < size:
    # Use a for loop to print the asterisks for each column in the row
    for _ in range(size):
        print("*", end="")  # Print asterisks without newlines
    # After printing the asterisks for one row, move to the next line
    print()
    # Increment the row count
    row += 1


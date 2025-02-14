# Define the number of rows for the triangle
triangleRows = 6

# Outer Loop to handle number of rows
for i in range(0, triangleRows):
    # Inner Loop to handle number of columns
    for j in range(0, i + 1):
        # Printing stars
        print("* ", end = "")
    # Ending line after each row
    print()


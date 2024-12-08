# Initialize the Sudoku grid with variables
sudoku_table = [[f"{chr(97 + row)}{col + 1}" for col in range(9)] for row in range(9)]

# Print the Sudoku table with formatting
print("Sudoku Table (9x9):")
print("-" * 37)  # Top border
for i, row in enumerate(sudoku_table):
    formatted_row = " | ".join(row)  # Add vertical separators
    print(f"| {formatted_row} |")  # Add borders on the sides
    if (i + 1) % 3 == 0 and i != 8:  # Add horizontal separators after every 3 rows
        print("-" * 37)
print("-" * 37)  # Bottom border

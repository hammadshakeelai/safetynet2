import random

# Function to print the Sudoku board
def print_sudoku(board):
    print("-" * 25)
    for i, row in enumerate(board):
        row_str = ""
        for j, num in enumerate(row):
            if j % 3 == 0:
                row_str += "| "
            row_str += f"{num if num != 0 else ' '} "
        row_str += "|"
        print(row_str)
        if (i + 1) % 3 == 0:
            print("-" * 25)

# Function to check if it's safe to place a number
def is_safe(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

# Function to fill the Sudoku board
def fill_board(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in random.sample(range(1, 10), 9):
                    if is_safe(board, i, j, num):
                        board[i][j] = num
                        if fill_board(board):
                            return True
                        board[i][j] = 0
                return False
    return True

# Function to remove numbers to create a puzzle
def remove_numbers(board, clues=30):
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    for i, j in cells:
        if clues <= 0:
            break
        temp = board[i][j]
        board[i][j] = 0
        board_copy = [row[:] for row in board]
        if not fill_board(board_copy):
            board[i][j] = temp
        clues -= 1

# Generate a Sudoku puzzle
def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    fill_board(board)
    remove_numbers(board)
    return board

# Function to check if the Sudoku is solved
def is_solved(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True

# Play the Sudoku game
def play_sudoku():
    puzzle = generate_sudoku()
    solution = [row[:] for row in puzzle]
    fill_board(solution)
    print("\nWelcome to Sudoku!")
    print("Solve the puzzle by entering your moves.")
    print("To exit the game, type 'exit'.")
    
    while not is_solved(puzzle):
        print_sudoku(puzzle)
        move = input("Enter your move (row, col, num): ").strip()
        if move.lower() == "exit":
            print("Exiting the game. Goodbye!")
            return
        try:
            row, col, num = map(int, move.split(","))
            if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
                print("Invalid input! Enter numbers between 1 and 9.")
                continue
            row, col = row - 1, col - 1
            if puzzle[row][col] != 0:
                print("Cell is already filled! Try another move.")
                continue
            if is_safe(puzzle, row, col, num) and solution[row][col] == num:
                puzzle[row][col] = num
                print("Move accepted!")
            else:
                print("Invalid move! Doesn't fit Sudoku rules or incorrect number.")
        except ValueError:
            print("Invalid input format! Use: row,col,num (e.g., 3,4,5).")

    print("Congratulations! You've solved the Sudoku!")
    print_sudoku(puzzle)

# Main program
if __name__ == "__main__":
    play_sudoku()

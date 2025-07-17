#make sudoku solver that solves users sudoku puzzle and prints the solved board in a nice format
# Sudoku Solver
# Function to print the Sudoku board
def print_board(board): 
    for i in range(9):
        row_str = ""
        for j in range(9):
            if board[i][j] == 0:
                row_str += ". "
            else:
                row_str += str(board[i][j]) + " "
            if (j + 1) % 3 == 0 and j != 8:
                row_str += "| "
        row_str = row_str.strip()
        print(row_str)
        if (i + 1) % 3 == 0 and i != 8:
            print("-" * 21)
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
# Function to solve the Sudoku board
def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_safe(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True
# Function to check if the Sudoku is solved
def is_solved(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False
    return True
# Function to get user input for the Sudoku puzzle
def get_user_input():
    board = [[0] * 9 for _ in range(9)]
def get_user_input():
    board = [[0] * 9 for _ in range(9)]
    print("Enter your Sudoku puzzle row by row, use 0 for empty cells:")
    for i in range(9):
        row_input = input(f"Row {i + 1}: ")
        # Accept either space-separated or just 9 digits
        if " " in row_input:
            numbers = list(map(int, row_input.strip().split()))
        else:
            numbers = [int(ch) for ch in row_input.strip()]
        if len(numbers) != 9:
            print("Each row must contain exactly 9 numbers.")
def main():
    board = get_user_input()
    
    if board is None:
        print("Invalid input. Please try again.")
        main()  # Restart if input is invalid
        return
    print("Initial Sudoku Puzzle:")
    print_board(board)
    if solve_sudoku(board):
        print("Solved Sudoku Puzzle:")
        print_board(board)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()  
if __name__ == "__main__":
    main()  
#####################################################################
# #make sudoku solver that solves users sudoku puzzle
# # Sudoku Solver
# import random   
# # Function to print the Sudoku board
# def print_board(board): 
#     for i in range(9):
#         row_str = ""
#         for j in range(9):
#             if board[i][j] == 0:
#                 row_str += ". "
#             else:
#                 row_str += str(board[i][j]) + " "
#             if (j + 1) % 3 == 0 and j != 8:
#                 row_str += "| "
#         row_str = row_str.strip()
#         print(row_str)
#         if (i + 1) % 3 == 0 and i != 8:
#             print("-" * 21)
# # Function to check if it's safe to place a number
# def is_safe(board, row, col, num):
#     for x in range(9):
#         if board[row][x] == num or board[x][col] == num:
#             return False
#     start_row, start_col = 3 * (row // 3), 3 * (col // 3)
#     for i in range(3):
#         for j in range(3):
#             if board[start_row + i][start_col + j] == num:
#                 return False
#     return True
# # Function to solve the Sudoku board
# def solve_sudoku(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 for num in range(1, 10):
#                     if is_safe(board, i, j, num):
#                         board[i][j] = num
#                         if solve_sudoku(board):
#                             return True
#                         board[i][j] = 0
#                 return False
#     return True
# # Function to check if the Sudoku is solved
# def is_solved(board):
#     for i in range(9):
#         for j in range(9):
#             if board[i][j] == 0:
#                 return False
#     return True
# # Function to get user input for the Sudoku puzzle
# def get_user_input():
#     board = [[0] * 9 for _ in range(9)]
#     print("Enter your Sudoku puzzle row by row, use 0 for empty cells:")
#     for i in range(9):
#         row_input = input(f"Row {i + 1}: ")
#         numbers = list(map(int, row_input.split()))
#         if len(numbers) != 9:
#             print("Each row must contain exactly 9 numbers.")
#             return None
#         board[i] = numbers
#     return board
# # Main function to run the Sudoku solver
# def main():
#     board = get_user_input()
    
#     if board is None:
#         print("Invalid input. Please try again.")
#         main()  # Restart if input is invalid
        
#         return
#     print("Initial Sudoku Puzzle:")
#     print_board(board)
#     if solve_sudoku(board):
#         print("Solved Sudoku Puzzle:")
#         print_board(board)
#     else:
#         print("No solution exists.")
# if __name__ == "__main__":
#     main()  
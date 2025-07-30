# Brute force function for validation of board
def is_valid(board):
    n = len(board)

    for i in range(n):
        for j in range(n):
            num = board[i][j]
            if num == 0:
                continue

            # Check left in the row
            for k in range(n):
                if k != j and board[i][k] == num:
                    return False

            # Check up in the column
            for k in range(n):
                if k != i and board[k][j] == num:
                    return False

            # Check 2x2 box
            box_start_row = (i // 2) * 2
            box_start_col = (j // 2) * 2
            for r in range(box_start_row, box_start_row + 2):
                for c in range(box_start_col, box_start_col + 2):
                    if (r != i or c != j) and board[r][c] == num:
                        return False

    return True

# Backtracking for partially solving
def solve_partial(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                for num in range(1, len(board) + 1):
                    board[row][col] = num
                    if is_valid(board) and solve_partial(board):
                        return True
                    board[row][col] = 0
                return False  # No valid number found
    return True  # Solved

# Board to solve
board = [
    [1, 0, 0, 0],
    [0, 0, 2, 1],
    [0, 3, 0, 0],
    [0, 0, 4, 0]
]

# Solve and print
if solve_partial(board):
    print("Solved board:")
    for row in board:
        print(row)
else:
    print("No solution found.")

import math

def evaluate(board):
    # Check rows, columns, and diagonals for a win or loss
    for row in board:
        if all(cell == 'X' for cell in row):
            return 1
        elif all(cell == 'O' for cell in row):
            return -1

    for col in range(3):
        if all(board[row][col] == 'X' for row in range(3)):
            return 1
        elif all(board[row][col] == 'O' for row in range(3)):
            return -1

    if all(board[i][i] == 'X' for i in range(3)) or all(board[i][2-i] == 'X' for i in range(3)):
        return 1
    elif all(board[i][i] == 'O' for i in range(3)) or all(board[i][2-i] == 'O' for i in range(3)):
        return -1

    return 0  # No winner, game is still ongoing

def is_terminal(board):
    # Check if the board is full or if someone has won
    return all(cell != '.' for row in board for cell in row) or evaluate(board) != 0

def get_empty_cells(board):
    # Return a list of coordinates for empty cells on the board
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == '.']

def alpha_beta(board, depth, alpha, beta, maximizing_player):
    if is_terminal(board) or depth == 0:
        return evaluate(board)

    if maximizing_player:
        max_eval = -math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            eval = alpha_beta(board, depth - 1, alpha, beta, False)
            board[i][j] = '.'  # Undo the move
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            eval = alpha_beta(board, depth - 1, alpha, beta, True)
            board[i][j] = '.'  # Undo the move
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        eval = alpha_beta(board, 8, -math.inf, math.inf, False)
        board[i][j] = '.'  # Undo the move
        if eval > best_eval:
            best_eval = eval
            best_move = (i, j)
    return best_move

# Example usage
board = [['X', '.', '.'],
         ['.', 'O', 'O'],
         ['X', 'X', 'O']]

best_move = find_best_move(board)
print(f"Optimal move: {best_move}")
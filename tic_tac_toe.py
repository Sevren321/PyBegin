def print_board(board):
    # Print the current state of the board
    for row in board:
        print(' | '.join(row))
        print('-' * 5)

def check_winner(board, player):
    # Check horizontal wins
    for row in board:
        if all([spot == player for spot in row]):
            return True

    # Check vertical wins
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonal wins
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_board_full(board):
    # Check if the board is full (draw condition)
    return all([spot != ' ' for row in board for spot in row])

def play_tic_tac_toe():
    # Initialize the empty board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        # Get player move 
        row = int(input(f"Player {current_player}, choose row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, choose column (0, 1, 2): "))
        

        # Check if the move is valid
        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("That spot is already taken. Try again.")
        
        # Check for a win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw 
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        print_board(board)
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()
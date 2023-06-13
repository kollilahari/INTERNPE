def print_board(board):
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i+3]))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]

    return None

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        position = int(input("Enter the position (1-9): ")) - 1

        if 0 <= position <= 8 and board[position] == " ":
            board[position] = current_player
            winner = check_winner(board)

            if winner:
                print(f"Player {winner} wins!")
                game_over = True
            elif all(cell != " " for cell in board):
                print("It's a tie!")
                game_over = True
            else:
                current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

play_game()

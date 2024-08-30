# Step 1: Set Up the Board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Step 2: Check for a Win
def check_win(board, mark):
    # Check rows, columns, and diagonals for a win
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [mark, mark, mark] in win_conditions

# Step 3: Take Player Input and Handle Game Logic
def play_game():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = "X"
    game_won = False

    for _ in range(9):
        print_board(board)
        move = input(f"Player {current_player}, choose your move (1-9): ")

        if move not in [str(num) for num in range(1, 10)]:
            print("Invalid move. Please try again.")
            continue

        move = int(move) - 1

        if board[move] in ["X", "O"]:
            print("This spot is already taken. Please try again.")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            game_won = True
            break

        current_player = "O" if current_player == "X" else "X"

    if not game_won:
        print_board(board)
        print("It's a draw!")

# Run the game
if __name__ == "__main__":
    play_game()

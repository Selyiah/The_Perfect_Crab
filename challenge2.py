# Below is the same program as in the example. Your
# challenge is to implement some improvements:

# 1. Right now users can place their tiles over the other
#    user's tiles. Prevent this.

# 2. Right now if the game reaches a draw with no more free
#    spaces, the game doesn't end. Make it end at that
#    point.

# 3. If you want a real challenge, try to rework this
#    program to support a 5x5 board rather than a 3x3 board.

# 4. If you're still not satisfied, try to rework this
#    program to take a parameter `board_size` and play a
#    game with a board of that size.

# This is getting really challenging now — and is entirely
# optional. Don't forget about your assessment!

def generate_groups(size):
  # Define the groups as specified
    groups = [
      # Rows
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
        [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],
        [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
        [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)],
        [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4)],

      # Columns
        [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
        [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
        [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
        [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
        [(0, 4), (1, 4), (2, 4), (3, 4), (4, 4)],

      # Diagonals (bottom-right)
        [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)],
        [(0, 1), (1, 2), (2, 3), (3, 4)],
        [(1, 0), (2, 1), (3, 2), (4, 3)],
        [(1, 1), (2, 2), (3, 3), (4, 4)],

      # Diagonals (bottom-left)
        [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)],
        [(0, 3), (1, 2), (2, 1), (3, 0)],
        [(0, 2), (1, 1), (2, 0)],
        [(0, 1), (1, 0)],
        [(1, 4), (2, 3), (3, 2), (4, 1)],
        [(1, 3), (2, 2), (3, 1), (4, 0)],
        [(2, 4), (3, 3), (4, 2)],
        [(2, 3), (3, 2), (4, 1)],
        [(3, 4), (4, 3)],
    ]
    return groups

def print_groups(groups):
    for group in groups:
        print(group)

def is_game_over(board):
    size = len(board)
    groups_to_check = generate_groups(size)

    for group in groups_to_check:
        if is_group_complete(board, *group):
            if are_all_cells_the_same(board, *group):
                print(f"Player {board[group[0][0]][group[0][1]]} wins!")
                return True

  # Check if the board is full (draw)
    if all(cell != "." for row in board for cell in row):
        print("It's a draw!")
        return True

    return False

def play_game():
    size = 5
    board = [["." for _ in range(size)] for _ in range(size)]
    player = "X"

    while not is_game_over(board):
        print(print_board(board))
        print(f"It's {player}'s turn.")

      # Input validation
        try:
            row = int(input(f"Enter a row (0-{size - 1}): "))
            column = int(input(f"Enter a column (0-{size - 1}): "))

            if row < 0 or row >= size or column < 0 or column >= size:
                print(f"Invalid input! Row and column must be between 0 and {size - 1}.")
                continue

            if not make_move(board, row, column, player):
                print("Invalid move! This tile has been played already, try again.")
                continue

            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input! Please enter numbers.")

    print(print_board(board))
    print("Game over!")

# Utility functions for the game to work correctly
def print_board(board):
    return "\n".join(" ".join(row) for row in board)

def make_move(board, row, column, player):
    if board[row][column] == ".":
        board[row][column] = player
        return True
    return False

def is_group_complete(board, *coordinates):
    return all(0 <= x < len(board) and 0 <= y < len(board) for x, y in coordinates)

def are_all_cells_the_same(board, *coordinates):
    values = {board[x][y] for x, y in coordinates}
    return len(values) == 1 and values != {"."}

print("Generating groups for a 5x5 board:")
groups = generate_groups(5)
print_groups(groups)  # Ensure this prints the groups correctly

print("Game time!")
play_game()

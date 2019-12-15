import heuristic  # For ai_turn


# Variables
# game_board = 2d array to simulate the game board
# player = 1 or 2 based on the player turn. 1 = player1, 2 = player2
# s_column = standard column
# s_row = standard row
# last_column = the column in which the last slot filled
# last_row = the row in which the last slot filled

# General Notes
# Board format = board[column][row]


def test_print(board):
    # Print board in raw array format
    # for i in board:
    #   print(str(i))
    # Print board in simulated format
    for row in range(s_row):
        print()
        for column in range(s_column):
            print(board[column][row], "| ", end="")
    print()


def generate_board():
    global s_row
    global s_column
    # Standard Connect 4 board dimensions
    s_row = 6
    s_column = 7

    # Populate board, fills the 2d array with 0 as the place holder value
    generated_board = [[0 for i in range(0, s_row)] for x in range(0, s_column)]
    return generated_board


def fill(board, column, player):
    global last_row
    global last_column
    # last value in column
    row = s_row - 1

    # Determines where is the bottom of the row
    for curr_row in range(0, s_row):
        if board[column][curr_row] != 0:
            continue
        else:
            row = curr_row
    board[column][row] = player
    last_row = row
    last_column = column


def check(column):  # Checks if the column is full

    # Checks if the top of the column is not 0, meaning a full column
    if game_board[column][0] != 0:
        return False
    else:
        return True


# Check winner
def four_in_row(player):
    # win_column
    if last_row <= 2:
        if game_board[last_column][last_row] == player and \
                game_board[last_column][last_row + 1] == player and \
                game_board[last_column][last_row + 2] == player and \
                game_board[last_column][last_row + 3] == player:
            return player
        else:
            pass
    # win_row_right
    if last_column <= 3:
        if game_board[last_column][last_row] == player and \
                game_board[last_column + 1][last_row] == player and \
                game_board[last_column + 2][last_row] == player and \
                game_board[last_column + 3][last_row] == player:
            return player
    # win_row_left
    if last_column >= 3:
        if game_board[last_column][last_row] == player and \
                game_board[last_column - 1][last_row] == player and \
                game_board[last_column - 2][last_row] == player and \
                game_board[last_column - 3][last_row] == player:
            return player
    # win_right_up_diagonal
    if last_column <= 3 <= last_row:
        if game_board[last_column][last_row] == player and \
                game_board[last_column + 1][last_row - 1] == player and \
                game_board[last_column + 2][last_row - 2] == player and \
                game_board[last_column + 3][last_row - 3] == player:
            return player
    # win_right_down_diagonal
    if last_column <= 3 and last_row <= 2:
        if game_board[last_column][last_row] == player and \
                game_board[last_column + 1][last_row + 1] == player and \
                game_board[last_column + 2][last_row + 2] == player and \
                game_board[last_column + 3][last_row + 3] == player:
            return player
    # win_left_up_diagonal
    if last_column >= 3 and last_row >= 3:
        if game_board[last_column][last_row] == player and \
                game_board[last_column - 1][last_row - 1] == player and \
                game_board[last_column - 2][last_row - 2] == player and \
                game_board[last_column - 3][last_row - 3] == player:
            return player
    # win_left_down_diagonal
    if last_column >= 3 and last_row <= 2:
        if game_board[last_column][last_row] == player and \
                game_board[last_column - 1][last_row + 1] == player and \
                game_board[last_column - 2][last_row + 2] == player and \
                game_board[last_column - 3][last_row + 3] == player:
            return player
    # no four in a row, returns zero
    return 0


def player_turn(player):
    # User input for which column
    while True:
        column = int(input("Player " + str(player) + " select column: ")) - 1
        if column not in range(0, s_column):
            print("Column does not exist")
        if not check(column):
            print("Slot is full, try another")
        else:
            break
    if check(column):
        fill(game_board, column, player)  # 1 meaning player1 for player


def ai_turn(player):
    column = heuristic.scoring(game_board, player)
    if check(column):
        fill(game_board, column, player)


def main():
    global game_board
    game_board = generate_board()
    test_print(game_board)
    winner = 0
    turn = 1
    while True:
        if turn == 1:
            player_turn(1)
            # ai_turn(1)
            winner = four_in_row(1)
            test_print(game_board)
            turn = 2

        elif turn == 2:
            player_turn(2)
            # ai_turn(2)
            winner = four_in_row(2)
            test_print(game_board)
            turn = 1

        if winner != 0:
            print("Winner :", winner)
            break


main()

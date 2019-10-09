# Variables
# board = 2d array to simulate the game board
# player = 1 or 2 based on the player turn. 1 = player1, 2 = player2
# s_column = standard column
# s_row = standard row

# General Notes
# Board format = board[column][row]


def test_print():
    for row in range(s_row):
        print()
        for column in range(s_column):
            print(board[column][row], " ", end="")
    print()


def temporary_test_board():
    global s_row
    global s_column
    s_row = 6
    s_column = 7
    return [[i + (x * 10) for i in range(1, s_row + 1)] for x in range(1, s_column + 1)]


def generate_board():
    global s_row
    global s_column
    # Standard Connect 4 board dimensions
    s_row = 6
    s_column = 7

    # Populate board
    game_board = [[0 for i in range(0, s_row)] for x in range(0, s_column)]
    return game_board


def fill(column, player):
    # last value in column
    row = s_row - 1

    # Determines where is the bottom of the row
    for curr_row in range(0, s_row):
        if board[column][curr_row] != 0:
            continue
        else:
            row = curr_row
    board[column][row] = player


def check(column):  # Checks if the column is full

    # Checks if the top of the column is not 0, meaning a full column
    if board[column][0] != 0:
        print("gaboleh")
        return False
    else:
        print("boleh")
        return True


def win_row(player):
    # print(s_row)
    # iterates through all the rows
    for row in range(s_row):

        # iterates through columns until the
        for column in range(s_column - 3):

            # checks if there is a row of 4 of the same "color"
            if board[column][row] == player and \
                    board[column + 1][row] == player and \
                    board[column + 2][row] == player and \
                    board[column + 3][row] == player:
                return player
    return 0


def win_column(player):

    # iterates through columns until the
    for column in range(s_column):

        # iterates through all the rows
        for row in range(s_row - 3):

            # checks if there is a column of 4 of the same "color"
            if board[column][row] == player and \
                    board[column][row + 1] == player and \
                    board[column][row + 2] == player and \
                    board[column][row + 3] == player:
                return player
    return 0


def player_turn(player):
    # User input for which column
    column = int(input("Select column: "))
    if check(column):
        fill(column, player)  # 1 meaning player1 for player


def ai_turn():
    # True
    pass


def main():
    global board

    board = generate_board()
    # board = temporary_test_board()
    print(board)
    # print(s_row)

    while True:
        player_turn(1)
        print(win_row(1) or win_column(1))
        player_turn(2)
        print(win_row(2) or win_column(2))
        print(board)
        ai_turn()
        # print(board)


main()

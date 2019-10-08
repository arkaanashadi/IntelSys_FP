# Variables
# board = 2d array to simulate the game board
# player = 1 or 2 based on the player turn. 1 = player1, 2 = player2
# column = self explanatory
# row = self explanatory


def generate_board():

    # Board Dimensions
    s_row = 6
    s_column = 7

    # Populate board
    game_board = [[0 for i in range(0, s_row)] for x in range(0, s_column)]
    return game_board


def fill(board, column, player):

    # last value in column
    row = len(board[column]) - 1

    # Determines where is the bottom of the row
    for curr_row in range(0, row + 1):
        if board[column][curr_row] != 0:
            continue
        else:
            row = curr_row
    board[column][row] = player


def check(board, column):  # Checks if the column is full

    # Checks if the top of the column is not 0, meaning a full column
    if board[column][0] != 0:
        print("gaboleh")
        return False
    else:
        print("boleh")
        return True


def win_row(board, player):
    pass


def player_turn(board):

    # User input for which column
    column = int(input("Select column:"))
    if check(board, column):
        fill(board, column, 1)


def ai_turn(board):
    # True
    pass


def main():
    board = generate_board()
    print(board)
    while True:
        player_turn(board)
        print(board)
        ai_turn(board)
        # print(board)


main()

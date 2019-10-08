# Variables
# board = 2d array to simulate the game board
# player = 1 or 2 based on the player turn. 1 = player1, 2 = player2
# s_column = standard column
# s_row = standard row


def generate_board():

    # Board Dimensions
    global s_row
    global s_column
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
    for row in len(board[0]):
        pass


def player_turn():

    # User input for which column
    column = int(input("Select column:"))
    if check(board, column):
        fill(board, column, 1)


def ai_turn(board):
    # True
    pass


def main():
    global board
    board = generate_board()
    print(board)
    print(len(board[0]))
    while True:
        player_turn(board)
        print(board)
        ai_turn(board)
        # print(board)


main()

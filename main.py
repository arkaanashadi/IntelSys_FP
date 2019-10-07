# import numpy as np


def generate_board():
    # s_row = int(input("row:"))
    # s_column = int(input("column:"))

    # Board Dimensions
    s_row = 6
    s_column = 7

    # Populate board
    game_board = [[0 for i in range(0, s_row)] for x in range(0, s_column)]
    return game_board
# def check_full(column):
#     print(board[-1][column])

# def player():
#     ch_column

# print(board[0][1])
# check_full(0)

def fill(column):
    pass

def check(board, column, row): # Checks if the column is full
    # print(board[column][row])

    # Checks if the top of the column is not 0, meaning a full column
    if board[column][row] != 0:
        print("gaboleh")
        return False
    else:
        print("boleh")
        return True

def player_turn(board):
    # User input for which row
    column = int(input("Select column:"))

    # Determines where is the bottom of the row
    row = len(board[0]) - 1
    for i in board[column]:
        if board[column][i] != 0:
            row = i
            break
        else:
            break
    check(board, column, row)

def ai_turn(board):
    True

def main():
    board = generate_board()
    print(board)
    player_turn(board)
    print(board)
    ai_turn(board)
    print(board)
main()

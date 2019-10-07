# import numpy as np


def generate_board():
    # s_row = int(input("row:"))
    # s_column = int(input("column:"))
    s_row = 6
    s_column = 7

    game_board = [[0 for i in range(0, s_row)] for x in range(0, s_column)]
    return game_board
    # for i in range(len(board)):
    #     print(board[i])


# def check_full(column):
#     print(board[-1][column])

# def player():
#     ch_column

# print(board[0][1])
# check_full(0)

def fill(column):

def check(board,column,row):
    print(board[column][row])
    if board[column][row] != 0:
        print("gaboleh")
        return False
    else:
        print("boleh")
        return True

def main():
    board = generate_board()
    print(board)
    column = int(input("Select column:"))
    row = len(board[0])-1
    for i in board[column]:
        if board[column][i] != 0:
            row = i
            break
        else:
            break
    check(board,column,row)
    print(board)
main()

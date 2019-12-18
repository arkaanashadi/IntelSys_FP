import numpy
import copy

def scoring(board, s_row, player):
    from CONN4 import fill
    # just to get the fill function, separate later
    ai_board = copy.deepcopy(board)
    score = [0] * len(ai_board)
    for ai_column in range(len(ai_board)):
        fill(ai_board, ai_column, s_row, player)
        score[ai_column] += minimax(ai_board, ai_column, get_row(ai_board, ai_column), player)
        # for i in ai_board:
        #     print(str(i))
        ai_board = copy.deepcopy(board)
        print(score)
    decision = score.index(max(score))
    return decision


def get_row(board, column):
    # Determines where is the bottom of the row
    for curr_row in range(0, len(board[0])):
        if board[column][curr_row] == 0:
            continue
        else:
            # print("curr row", curr_row)
            return curr_row


def minimax(board, column, row, player):
    if four_in_row(board, column, row, player):
        return numpy.inf
    #elif centre(board, column, row, player):
    #    return 4
    elif three_in_row(board, column, row, player):
        return 3
    elif two_in_row(board, column, row, player):
        return 2
    return 0


def default():
    return 0


########################################################################################################################
# Check two in a row
def two_in_row(board, column, row, player):
    # two_column
    if row <= 4:
        if board[column][row] == player and \
                board[column][row + 1] == player:
            return True
        else:
            pass
    # two_row_right
    if column <= 4:
        if board[column][row] == player and \
                board[column + 1][row] == player:
            return True
    # two_row_left
    if column >= 1:
        if board[column][row] == player and \
                board[column - 1][row] == player:
            return True
    # two_right_up_diagonal
    if column <= 5 and row >= 1:
        if board[column][row] == player and \
                board[column + 1][row - 1] == player:
            return True
    # two_right_down_diagonal
    if column <= 5 and row <= 4:
        if board[column][row] == player and \
                board[column + 1][row + 1] == player:
            return True
    # two_left_up_diagonal
    if column >= 1 and row >= 1:
        if board[column][row] == player and \
                board[column - 1][row - 1] == player:
            return True
    # two_left_down_diagonal
    if column >= 1 and row <= 4:
        if board[column][row] == player and \
                board[column - 1][row + 1] == player:
            return True
    # no two in a row, False
    return False


########################################################################################################################
# Check three in a row
def three_in_row(board, column, row, player):
    # three_column
    if row <= 3:
        if board[column][row] == player and \
                board[column][row + 1] == player and \
                board[column][row + 2] == player:
            return True
        else:
            pass
    # three_row_right
    if column <= 4:
        if board[column][row] == player and \
                board[column + 1][row] == player and \
                board[column + 2][row] == player:
            return True
    # three_row_left
    if column >= 2:
        if board[column][row] == player and \
                board[column - 1][row] == player and \
                board[column - 2][row] == player:
            return True
    # three_right_up_diagonal
    if column <= 4 and row >= 2:
        if board[column][row] == player and \
                board[column + 1][row - 1] == player and \
                board[column + 2][row - 2] == player:
            return True
    # three_right_down_diagonal
    if column <= 4 and row <= 3:
        if board[column][row] == player and \
                board[column + 1][row + 1] == player and \
                board[column + 2][row + 2] == player:
            return True
    # three_left_up_diagonal
    if column >= 2 and row >= 2:
        if board[column][row] == player and \
                board[column - 1][row - 1] == player and \
                board[column - 2][row - 2] == player:
            return True
    # three_left_down_diagonal
    if column >= 2 and row <= 3:
        if board[column][row] == player and \
                board[column - 1][row + 1] == player and \
                board[column - 2][row + 2] == player:
            return True
    # no three in a row, False
    return False


########################################################################################################################
# Check four in a row
def four_in_row(board, column, row, player):
    # win_column
    if row <= 2:
        if board[column][row] == player and \
                board[column][row + 1] == player and \
                board[column][row + 2] == player and \
                board[column][row + 3] == player:
            return True
        else:
            pass
    # win_row_right
    if column <= 3:
        if board[column][row] == player and \
                board[column + 1][row] == player and \
                board[column + 2][row] == player and \
                board[column + 3][row] == player:
            return True
    # win_row_left
    if column >= 3:
        if board[column][row] == player and \
                board[column - 1][row] == player and \
                board[column - 2][row] == player and \
                board[column - 3][row] == player:
            return True
    # win_right_up_diagonal
    if column <= 3 <= row:
        if board[column][row] == player and \
                board[column + 1][row - 1] == player and \
                board[column + 2][row - 2] == player and \
                board[column + 3][row - 3] == player:
            return True
    # win_right_down_diagonal
    if column <= 3 and row <= 2:
        if board[column][row] == player and \
                board[column + 1][row + 1] == player and \
                board[column + 2][row + 2] == player and \
                board[column + 3][row + 3] == player:
            return True
    # win_left_up_diagonal
    if column >= 3 and row >= 3:
        if board[column][row] == player and \
                board[column - 1][row - 1] == player and \
                board[column - 2][row - 2] == player and \
                board[column - 3][row - 3] == player:
            return True
    # win_left_down_diagonal
    if column >= 3 and row <= 2:
        if board[column][row] == player and \
                board[column - 1][row + 1] == player and \
                board[column - 2][row + 2] == player and \
                board[column - 3][row + 3] == player:
            return True
    # no four in a row, False
    return False


def centre(board, column, row, player):
    # centre_slot
    print(row)
    print(row-1)
    if board[column][row] == player and \
            board[int(len(board)/2)][row] == player:
        return True
    # no four in a row, False
    return False

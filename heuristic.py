import numpy
import copy

def scoring(board, s_row, player, curr_score):
    from CONN4 import fill
    # just to get the fill function, separate later
    ai_board = copy.deepcopy(board)
    score = copy.deepcopy(curr_score)
    opponent = int
    if player == 1:
        opponent = 2
    elif player == 2:
        opponent = 1
    for ai_column in range(len(ai_board)):
        fill(ai_board, ai_column, s_row, player)
        point = minimax(ai_board, ai_column, get_row(ai_board, ai_column), player)        # check all possibilities
        score[ai_column] += point
        # Opponent's next move total deduction scoring , unfinished
        fill(ai_board, ai_column, s_row, opponent)
        minpoint = minimax(ai_board,ai_column, get_row(ai_board,ai_column) - 1, opponent)
        score[ai_column] -= minpoint
        print(point)
        print(minpoint)
        for i in ai_board:
            print(str(i))
        ai_board = copy.deepcopy(board)
        print(score)
    return score


def get_row(board, column):
    # Determines where is the bottom of the row
    for curr_row in range(0, len(board[0])):
        if board[column][curr_row] == 0:
            continue
        else:
            # print("curr row", curr_row)
            return curr_row


def minimax(board, column, row, player):
    total_points = 0
    if four_in_row(board, column, row, player):
        return numpy.inf
    total_points += three_in_row(board, column, row, player)
    total_points += two_in_row(board, column, row, player)
    return total_points


########################################################################################################################
# Check two in a row
def two_in_row(board, column, row, player):
    two_rows = 0
    # two_column
    if row <= 4:
        if board[column][row] == player and \
                board[column][row + 1] == player:
            board[column][row + 1] = 0
            two_rows += 2
        else:
            pass
    # two_row_right
    if column <= 4:
        if board[column][row] == player and \
                board[column + 1][row] == player:
            board[column][row + 1] = 0
            two_rows += 2
    # two_row_left
    if column >= 1:
        if board[column][row] == player and \
                board[column - 1][row] == player:
            board[column][row - 1] = 0
            two_rows += 2
    # two_right_up_diagonal
    if column <= 5 and row >= 1:
        if board[column][row] == player and \
                board[column + 1][row - 1] == player:
            board[column + 1][row - 1] = 0
            two_rows += 2
    # two_right_down_diagonal
    if column <= 5 and row <= 4:
        if board[column][row] == player and \
                board[column + 1][row + 1] == player:
            board[column + 1][row + 1] = 0
            two_rows += 2
    # two_left_up_diagonal
    if column >= 1 and row >= 1:
        if board[column][row] == player and \
                board[column - 1][row - 1] == player:
            board[column - 1][row - 1] = 0
            two_rows += 2
    # two_left_down_diagonal
    if column >= 1 and row <= 4:
        if board[column][row] == player and \
                board[column - 1][row + 1] == player:
            board[column - 1][row + 1] = 0
            two_rows += 2
    # no two in a row, False
    return two_rows


########################################################################################################################
# Check three in a row
def three_in_row(board, column, row, player):
    three_rows = 0
    # three_column
    if row <= 3:
        if board[column][row] == player and \
                board[column][row + 1] == player and \
                board[column][row + 2] == player:
            three_rows += 3
        else:
            pass
    # three_row_right
    if column <= 4:
        if board[column][row] == player and \
                board[column + 1][row] == player and \
                board[column + 2][row] == player:
            three_rows += 3
    # three_row_left
    if column >= 2:
        if board[column][row] == player and \
                board[column - 1][row] == player and \
                board[column - 2][row] == player:
            three_rows += 3
    # three_right_up_diagonal
    if column <= 4 and row >= 2:
        if board[column][row] == player and \
                board[column + 1][row - 1] == player and \
                board[column + 2][row - 2] == player:
            three_rows += 3
    # three_right_down_diagonal
    if column <= 4 and row <= 3:
        if board[column][row] == player and \
                board[column + 1][row + 1] == player and \
                board[column + 2][row + 2] == player:
            three_rows += 3
    # three_left_up_diagonal
    if column >= 2 and row >= 2:
        if board[column][row] == player and \
                board[column - 1][row - 1] == player and \
                board[column - 2][row - 2] == player:
            three_rows += 3
    # three_left_down_diagonal
    if column >= 2 and row <= 3:
        if board[column][row] == player and \
                board[column - 1][row + 1] == player and \
                board[column - 2][row + 2] == player:
            three_rows += 3
    # no three in a row, False
    return three_rows


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

def center():
    return 4

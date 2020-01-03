import copy


def terminal(board, board_score, curr_index, targetindex, terminaldata, s_row, ai_column, player, curr_depth, targetdepth):
    from CONN4 import fill
    ai_board = copy.deepcopy(board)  # AI's "imaginative" board
    score = copy.deepcopy(board_score)
    terminal_list = copy.deepcopy(terminaldata)
    opponent = int
    if player == 1:
        opponent = 2
    elif player == 2:
        opponent = 1

    print("PLAYER#######################################################")
    print(player)
    print("CURRENT DEPTH = "+ str(curr_depth))
    print("TARGET DEPTH = " + str(targetdepth))
    print("CURRENT INDEX = "+ str(curr_index))
    print("TARGET INDEX = " + str(targetindex))
    print("LEAF NODE @@@@@@@@@@@@")
    print(len(terminal_list))
    print("SCORE @@@@@@@")
    print(len(score))

    terminal_board = copy.deepcopy(ai_board)
    fill(terminal_board, ai_column, s_row, player)
    terminal_list.append(terminal_board)

    fill(ai_board, ai_column, s_row, player)
    for i in ai_board:
        print('\033[91m'+str(i)+'\033[0m')
    score[ai_column] += scoring(ai_board, ai_column, get_row(ai_board, ai_column), player)
    for index in range(len(ai_board)):
        score.append(score[index])
    print("maximize point = " + str(score[ai_column]))
    ai_board = copy.deepcopy(board)
    score[ai_column] = copy.deepcopy(board_score[ai_column])
    for i in [score[c:c + 7] for c in range(0, len(score), 7) if c % 5 == 0]:
        print(*i)

    if curr_index == targetindex:   # Generate board for the next depth of tree
        del terminal_list[:1]
        del score[:len(ai_board)]
        print("POST PROCESSING")
        print("LEAF NODE @@@@@@@@@@@@")
        print(len(terminal_list))
        for i in terminal_list:
            print(i)
        print("SCORE @@@@@@@")
        print(len(score))
        if curr_depth == targetdepth:
            return minimax(score, 0, True, 0, targetdepth+1)
        else:
            return terminal(terminal_list[0], score, 0, ((targetindex+1) * len(terminal_list)-1),
                        terminal_list, s_row, 0, opponent, curr_depth + 1, targetdepth)
    else:   # Generate boards for the next terminal index
        if curr_index != 0 and (curr_index+1)%len(board) == 0:
            del terminal_list[:1]
            del score[:len(ai_board)]
            return terminal(terminal_list[0], score, curr_index + 1, targetindex, terminal_list, s_row, 0,
                            player, curr_depth, targetdepth)
        else:
            return terminal(terminal_list[0], score, curr_index + 1, targetindex, terminal_list, s_row, ai_column + 1, player, curr_depth, targetdepth)


def minimax(score, index, maxturn, curr_depth, targetdepth):
    print("##########################################################################################################")
    print("index = "+str(index))
    print("current depth = "+str(curr_depth))
    print("target depth = "+str(targetdepth))
    print("len of score = "+str(len(score)))
    if curr_depth == targetdepth:
        print("score = "+ str(score[index]))
        return score[index]
    if maxturn:
        print("MAX")
        # Maximize score, determine the best column to fill
        return max(minimax(score, index * 7, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 1, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 2, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 3, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 4, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 5, False, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 6, False, curr_depth + 1, targetdepth))
    else:
        print("MIN")
        # Minimize
        return min(minimax(score, index * 7, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 1, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 2, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 3, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 4, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 5, True, curr_depth + 1, targetdepth),
                   minimax(score, index * 7 + 6, True, curr_depth + 1, targetdepth))
    # ai_board = copy.deepcopy(board) # Reset AI's board to the real one
    # return score # Give out the score of all columns


def get_row(board, column):
    # Determines where is the bottom of the row
    for curr_row in range(0, len(board[0])):
        if board[column][curr_row] == 0:
            continue
        else:
            # print("curr row", curr_row)
            return curr_row


def scoring(board, column, row, player):  # Calculate the total score of a column
    total_points = 0
    if four_in_row(board, column, row, player):
        return 200
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
            board[column + 1][row] = 0
            two_rows += 2
    # two_row_left
    if column >= 1:
        if board[column][row] == player and \
                board[column - 1][row] == player:
            board[column - 1][row] = 0
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
    return 3

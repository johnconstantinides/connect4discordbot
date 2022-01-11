from typing import List


def print_board(board) -> str:
    line = f"""
    {board[0][0]}{board[0][1]}{board[0][2]}{board[0][3]}{board[0][4]}{board[0][5]}{board[0][6]}
{board[1][0]}{board[1][1]}{board[1][2]}{board[1][3]}{board[1][4]}{board[1][5]}{board[1][6]}
{board[2][0]}{board[2][1]}{board[2][2]}{board[2][3]}{board[2][4]}{board[2][5]}{board[2][6]}
{board[3][0]}{board[3][1]}{board[3][2]}{board[3][3]}{board[3][4]}{board[3][5]}{board[3][6]}
{board[4][0]}{board[4][1]}{board[4][2]}{board[4][3]}{board[4][4]}{board[4][5]}{board[4][6]}
{board[5][0]}{board[5][1]}{board[5][2]}{board[5][3]}{board[5][4]}{board[5][5]}{board[5][6]}
    """
    return line

def has_won(board,row,column,piece) -> bool:

    #vertical check
    for i in range(3):
        if board[i][row] == piece and board[i + 1][row] == piece and board[i + 2][row] == piece and board[i + 3][row] == piece:
            return True
    #horizontal check
    for i in range(4):
        if board[column][i] == piece and board[column][i + 1] == piece and board[column][i + 2] == piece and board[column][i + 3] == piece:
                return True
    


    #split it up board into 4 quadrants where 2 quadrants over lap by the middle row
    if row <= 3 and column > 2:
        if row == 0 or column == 5:
            if piece == board[column][row] == board[column -1][row +1] == board[column -2][row + 2] == board[column -3][row + 3]:
                return True
        else:
            while row != 0 and column != 5:
                row -= 1
                column += 1
            while row <=3 and column > 2:
                if piece == board[column][row] == board[column -1][row +1] == board[column -2][row + 2] == board[column -3][row + 3]:
                    return True
                row += 1
                column -= 1
    elif row <= 3 and column < 3:
        if row == 0 or column == 0:
            if piece == board[column][row] == board[column + 1][row +1] == board[column + 2][row + 2] == board[column + 3][row + 3]:
                return True
        else:
            while row !=0 and column != 0:
                row -= 1
                column -= 1
            while row <= 2 and column < 3:
                if piece == board[column][row] == board[column + 1][row +1] == board[column + 2][row + 2] == board[column + 3][row + 3]:
                    return True
                row += 1
                column += 1
    elif row >= 3 and column > 2:
        if row == 6 or column == 5:
            if piece == board[column][row] == board[column - 1][row - 1] == board[column - 2][row - 2] == board[column - 3][row - 3]:
                return True
        else:
            while row != 6 and column != 5:
                row += 1
                column += 1
            while row >= 3 and column > 2:
                if piece == board[column][row] == board[column - 1][row - 1] == board[column - 2][row - 2] == board[column - 3][row - 3]:
                    return True
                row -= 1
                column -= 1
    elif row >=3 and column < 3:
        if row == 6 or column == 0:
            if piece == board[column][row] == board[column + 1][row - 1] == board[column + 2][row - 2] == board[column + 3][row - 3]:
                return True
        else:
            while row != 6 and column !=0:
                row += 1
                column -= 1
            while row >=3 and column < 3:
                if piece == board[column][row] == board[column + 1][row - 1] == board[column + 2][row - 2] == board[column + 3][row - 3]:
                    return True


    return False

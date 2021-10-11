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

def has_won(board,column,row,piece) -> bool:

    #vertical check
    for i in range(3):
        if board[i][column] == piece and board[i + 1][column] == piece and board[i + 2][column] == piece and board[i + 3][column] == piece:
            return True
    #horizontal check
    for i in range(4):
        if board[row][i] == piece and board[row][i + 1] == piece and board[row][i + 2] == piece and board[row][i + 3] == piece:
                return True
    
    #diagonal check
    if(row >= 3):
        if(column <=3):
            if board[row][column] == piece and board[row-1][column-1] == piece and board[row-2][column-2] == piece and board[row - 3][column - 3] == piece:
                return True
        if(column >= 3):
            return True


    return False

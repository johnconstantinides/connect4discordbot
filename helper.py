from typing import List


def print_board(board) -> str:
    line = f"""
    {board[0]}{board[1]}{board[2]}{board[3]}{board[4]}{board[5]}{board[6]}
{board[7]}{board[8]}{board[9]}{board[10]}{board[11]}{board[12]}{board[13]}
{board[14]}{board[15]}{board[16]}{board[17]}{board[18]}{board[19]}{board[20]}
{board[21]}{board[22]}{board[23]}{board[24]}{board[25]}{board[26]}{board[27]}
{board[28]}{board[29]}{board[30]}{board[31]}{board[32]}{board[33]}{board[34]}
{board[35]}{board[36]}{board[37]}{board[38]}{board[39]}{board[40]}{board[41]}
    """
    return line

def has_won(board,place,piece) -> bool:

    #vertical check
    row = place % 7
    for i in range(3):
        if board[i * 7 + row] == piece and board[i * 7 +row +7] == piece and board[i * 7 +row+14] == piece and board[i * 7+row+21] == piece:
            return True

    #horizontal check
    column = place // 7
    column = column * 7
    for i in range(4):
        if board[i + column] == piece and board[i + column + 1] == piece and board[i + column + 2] == piece and board[i + column +3] == piece:
                return True
    
    #diagonal check

    return False

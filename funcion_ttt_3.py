board = [[" "," "," "],[" "," "," "],[" "," "," "]]


def check_win (board, symbol):
    """Check if someone win"""
    # HORIZONTAL WINS
    if board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol:
                    return True
    if board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol:
                    return True             
    if board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol:
                    return True
                    
    # VERTICAL WINS
    if board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol:
                    return True               
    if board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol:
                    return True                 
    if board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol:
                    return True
                    
    # DIAGONAL WINS
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
                    return True                  
    if board[2][0] == symbol and board[1][1] == symbol and board[0][2] == symbol:
                    return True
    
    return False


def printed_board(board):
        """Print the board."""
        i = 0
        for row in board:            
            print("|".join(row))
            print("-----")


import os

def print_tic_tac_toe(position, tic_tac_toe):
    print(f"""
 Position      
 Available\t   Board
 {position[0]} | {position[1]} | {position[2]}\t {tic_tac_toe[0]} | {tic_tac_toe[1]} | {tic_tac_toe[2]}
---+---+---\t---+---+---
 {position[3]} | {position[4]} | {position[5]}\t {tic_tac_toe[3]} | {tic_tac_toe[4]} | {tic_tac_toe[5]}
---+---+---\t---+---+---
 {position[6]} | {position[7]} | {position[8]}\t {tic_tac_toe[6]} | {tic_tac_toe[7]} | {tic_tac_toe[8]}
""")

def rules_tic_tac_toe(tic_tac_toe):
    aux = ('X', 'O')
    for i, x in enumerate(aux):
        if (tic_tac_toe[:3].count(x) == 3) or \
                (tic_tac_toe[3:6].count(x) == 3) or \
                (tic_tac_toe[6:].count(x) == 3) or \
                (tic_tac_toe[::3].count(x) == 3) or \
                (tic_tac_toe[1::3].count(x) == 3) or \
                (tic_tac_toe[2::3].count(x) == 3) or \
                (tic_tac_toe[::4].count(x) == 3) or \
                (tic_tac_toe[2::2][:-1].count(x) == 3):
            print(f"{x} Wins!")
            return i + 1
    return 0

def play_game():
    """
    The code provided is a simple implementation of the Tic Tac Toe game in Python. 

The  `print_tic_tac_toe`  function takes in two lists as parameters:  `position`  and  `tic_tac_toe` . It prints the current state of the game board by displaying the positions and the corresponding values in the Tic Tac Toe board.

The  `rules_tic_tac_toe`  function checks if any player has won the game by checking all possible winning combinations. It returns 1 if player X wins, 2 if player O wins, and 0 if no player has won yet.

The  `play_game`  function is the main function that runs the game. It initializes the Tic Tac Toe board and position list. It then enters a loop that allows players to take turns entering their moves. The loop continues for a maximum of 9 turns. After each turn, the game board is printed and the  `rules_tic_tac_toe`  function is called to check if a player has won. If a player has won, the loop is broken and the winner is announced. If no player wins after 9 turns, the game ends in a draw.

Overall, the code provides a basic implementation of the Tic Tac Toe game. However, it lacks input validation and error handling, which could be added to improve the user experience.
    """
    tic_tac_toe = [' ', ' ', ' ',
                   ' ', ' ', ' ',
                   ' ', ' ', ' ']
    position = list(range(9))
    for _ in range(9):
        print_tic_tac_toe(position, tic_tac_toe)
        if _ % 2 == 0:
            turn = "X"
        else:
            turn = "O"
        aux = int(input(f"{turn} turn: ")) % 9
        tic_tac_toe[aux] = turn
        position[aux] = '*'
        if rules_tic_tac_toe(tic_tac_toe):
            break
        os.system('clear')
    else:
        print("No one wins...")
    print_tic_tac_toe(position, tic_tac_toe)

play_game()
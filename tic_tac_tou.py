tic_tac_toe = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
attempts = 0
print("Let's play tic-tac-toe...")
print("(Enter 'q' anytime to finish the game)")
print(f"""
{tic_tac_toe[0][0]}|{tic_tac_toe[0][1]}|{tic_tac_toe[0][2]}
-----
{tic_tac_toe[1][0]}|{tic_tac_toe[1][1]}|{tic_tac_toe[1][2]}
-----
{tic_tac_toe[2][0]}|{tic_tac_toe[2][1]}|{tic_tac_toe[2][2]}
""")
while attempts < 9:
    symbol = input("Choose a symbol: x/o ")
    # Check if the symbol is in the correct format
    if symbol == "q":
        print("GAME OVER")
        break
    if symbol != "x" and symbol != "o":
        print("""
    Wrong symbol.. choose another..""")
        continue
    # Choose the position for the symbol and check if it's in the correct range
    row = input("Choose a row (0-2): ")
    if row == "q":
        print("GAME OVER")
        break
    row = int(row)
    if row not in range(0, 3):
        print("""
    Wrong position.. choose in the range""")
        continue
    column = input("Choose a column (0-2): ")
    if column == "q":
        print("GAME OVER")
        break
    column = int(column)
    if column not in range(0, 3):
        print("""
    Wrong position.. choose in the range""")
        continue
    # Check if the chosen position is already taken
    if tic_tac_toe[row][column] == "x" or tic_tac_toe[row][column] == "o":
        print(f"""
    This position is already taken.. choose another..""")
        continue
    # Insert the symbol in the chosen position
    tic_tac_toe[row][column] = symbol
    # HORIZONTAL WINS
    if tic_tac_toe[0][0] == symbol and tic_tac_toe[0][1] == symbol and tic_tac_toe[0][2] == symbol:
        print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
        break
    if tic_tac_toe[1][0] == symbol and tic_tac_toe[1][1] == symbol and tic_tac_toe[1][2] == symbol:
        print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
        break
    if tic_tac_toe[2][0] == symbol and tic_tac_toe[2][1] == symbol and tic_tac_toe[2][2] == symbol:
        print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
        break
    # VERTICAL WINS
    if tic_tac_toe[0][0] == symbol and tic_tac_toe[1][0] == symbol and tic_tac_toe[2][0] == symbol:
        print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
        break
    if tic_tac_toe[0][1] == symbol and tic_tac_toe[1][1] == symbol and tic_tac_toe[2][1] == symbol:
        print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
        break
    if tic_tac_toe[0][2] == symbol and tic_tac_toe[1][2] == symbol and tic_tac_toe[2][2] == symbol:
        print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
        break
    # DIAGONAL WINS
    if tic_tac_toe[0][0] == symbol and tic_tac_toe[1][1] == symbol and tic_tac_toe[2][2] == symbol:
        print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
        break
    if tic_tac_toe[2][0] == symbol and tic_tac_toe[1][1] == symbol and tic_tac_toe[0][2] == symbol:
        print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
        break
    # PARTIAL IMPRESSION
    print(f"""
    {tic_tac_toe[0][0]}|{tic_tac_toe[0][1]}|{tic_tac_toe[0][2]}
    -----
    {tic_tac_toe[1][0]}|{tic_tac_toe[1][1]}|{tic_tac_toe[1][2]}
    -----
    {tic_tac_toe[2][0]}|{tic_tac_toe[2][1]}|{tic_tac_toe[2][2]}
    """)
    attempts += 1
# FINAL IMPRESSION   
print(f"""
    {tic_tac_toe[0][0]}|{tic_tac_toe[0][1]}|{tic_tac_toe[0][2]}
    -----
    {tic_tac_toe[1][0]}|{tic_tac_toe[1][1]}|{tic_tac_toe[1][2]}
    -----
    {tic_tac_toe[2][0]}|{tic_tac_toe[2][1]}|{tic_tac_toe[2][2]}
    """)
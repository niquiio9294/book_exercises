tic_tac_tou = [[" "," "," "],[" "," "," "],[" "," "," "]]
attempts = 0

print("Lest's play tic-tac-tou...")
print("(Enter 'q' anytime to finish the game)")
print(f"""
{tic_tac_tou[0][0]}|{tic_tac_tou[0][1]}|{tic_tac_tou[0][2]}
-----
{tic_tac_tou[1][0]}|{tic_tac_tou[1][1]}|{tic_tac_tou[1][2]}
-----
{tic_tac_tou[2][0]}|{tic_tac_tou[2][1]}|{tic_tac_tou[2][2]}
""")


while attempts < 9:
        symbol = input("Choose a symbol: x/o ")
    # we check if the symbol is in the correct format
        if symbol == "q":
                print("GAME OVER")
                break
        if symbol != "x" and symbol != "o":
                print("""
    Wrong symbol.. choose another..""")
                continue
        
    # now we choose the position to the symbol
    # and check if in the correct range
        row = input("Choose a row (0-2): ")
        if row == "q":
                print("GAME OVER")
                break
        row = int(row)
        if row not in range(0,3):
                print("""
    Wrong position.. choose in the range""")
                continue
        
        column = input("Choose a column (0-2): ")
        if column == "q":
                print("GAME OVER")
                break
        column = int(column)
        if column not in range(0,3):
                print("""
    Wrong position.. choose in the range""")
                continue


    # we check if the choosen position is already taken
        if tic_tac_tou[row][column] == "x" or tic_tac_tou[row][column] == "o":
            print(f"""
    This position is alredy taken.. choose another..""")
            continue
    # insert the symbol in the choosen position
        tic_tac_tou[row][column] = symbol

    # HORIZONTAL WINS
        if tic_tac_tou[0][0] == symbol and tic_tac_tou[0][1] == symbol and tic_tac_tou[0][2] == symbol:
                    print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
                    break
        if tic_tac_tou[1][0] == symbol and tic_tac_tou[1][1] == symbol and tic_tac_tou[1][2] == symbol:
                    print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
                    break
        if tic_tac_tou[2][0] == symbol and tic_tac_tou[2][1] == symbol and tic_tac_tou[2][2] == symbol:
                    print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
                    break
        
    # VERTICAL WINS
        if tic_tac_tou[0][0] == symbol and tic_tac_tou[1][0] == symbol and tic_tac_tou[2][0] == symbol:
                    print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
                    break
        if tic_tac_tou[0][1] == symbol and tic_tac_tou[1][1] == symbol and tic_tac_tou[2][1] == symbol:
                    print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
                    break
        if tic_tac_tou[0][2] == symbol and tic_tac_tou[1][2] == symbol and tic_tac_tou[2][2] == symbol:
                    print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
                    break

    # DIAGONAL WINS
        if tic_tac_tou[0][0] == symbol and tic_tac_tou[1][1] == symbol and tic_tac_tou[2][2] == symbol:
                    print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
                    break
        if tic_tac_tou[2][0] == symbol and tic_tac_tou[1][1] == symbol and tic_tac_tou[0][2] == symbol:
                    print(f"""
    Congrats!!! the symbol '{symbol}' wins..""")
                    break

    # PARTIAL IMPRESSION
        print(f"""
    {tic_tac_tou[0][0]}|{tic_tac_tou[0][1]}|{tic_tac_tou[0][2]}
    -----
    {tic_tac_tou[1][0]}|{tic_tac_tou[1][1]}|{tic_tac_tou[1][2]}
    -----
    {tic_tac_tou[2][0]}|{tic_tac_tou[2][1]}|{tic_tac_tou[2][2]}
    """)
        attempts += 1
        

 # FINAL IMPRESSION   
print(f"""
    {tic_tac_tou[0][0]}|{tic_tac_tou[0][1]}|{tic_tac_tou[0][2]}
    -----
    {tic_tac_tou[1][0]}|{tic_tac_tou[1][1]}|{tic_tac_tou[1][2]}
    -----
    {tic_tac_tou[2][0]}|{tic_tac_tou[2][1]}|{tic_tac_tou[2][2]}
    """)
                




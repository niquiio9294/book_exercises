def choose():
    """Function to enter ROCK, PAPER or SCISORS"""
    while True:
        player = input("\nEnter your move: (r)ock (p)aper (s)cissors or (q)uit ")
        if player == "r":
            player = "ROCK"
            break
        elif player == "p":
            player = "PAPER"
            break
        elif player == "s":
            player = "SCISSORS"
            break
        elif player == "q":
            break
        else:
            print("\nYour enter is wrong.. try again..")
            continue
    return player


def final_result(player, cpu):
    """Return us if player WIN, TIE or LOSE."""
    if player == cpu:
        result = "TIE"
    elif player == "ROCK" and cpu == "SCISSORS":
        result = "WIN"
    elif player == "PAPER" and cpu == "ROCK":
        result = "WIN"
    elif player == "SCISSORS" and cpu == "PAPER":
        result = "WIN"
    else:
        result = "LOSE"
    return result


def counter(result, win, tie, lose):
    """Keep score."""
    if result == "WIN":
        win += 1
    elif result == "TIE":
        tie += 1
    elif result == "LOSE":
        lose += 1
    return win, tie, lose

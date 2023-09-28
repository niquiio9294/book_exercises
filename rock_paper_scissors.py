import random
import funcion_rps

list = ["ROCK", "PAPER", "SCISSORS"]
win = 0
lose = 0
tie = 0

while True:
    print("ROCK, PAPER, SCISSORS")
    print(f"""{win} Wins, {lose} Losses, {tie} Ties""")

    player = funcion_rps.choose()
    if player == "q":
        print("\nGAME OVER")
        break   
    cpu = random.choice(list)

    result = funcion_rps.final_result(player, cpu)

    score = funcion_rps.counter(result, win, tie, lose)
    win = score[0]
    tie = score[1]
    lose = score[2]

    print(f"""
{player} versus ....
{cpu}""")
    print(f"""
It's a {result}!
""")
    
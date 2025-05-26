import random

options = ["paper", "rock", "scissors"]

playing = True
while playing:

    while True:
        player_choose = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
        if player_choose == 'q':
            playing = False
            break
        if player_choose in options:
            break
        else:
            print("Invalid input!!! Please type again:")
    if not playing:
        print("Thanks for playing!")
        break

    player_option_index = options.index(player_choose)
    bot_choose = random.randint(0,2)
    if (player_option_index == bot_choose + 1) or (player_option_index == 0 and bot_choose == 2):
        result = "You lose"
    elif (player_option_index == bot_choose - 1) or (player_option_index == 2 and bot_choose == 0):
        result = "You win"
    else:
        result = "Tie"

    print("You choose", player_choose.upper(), "and the bot choose", options[bot_choose].upper(), "-->",result)

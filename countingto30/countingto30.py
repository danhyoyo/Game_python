print("Choosing who will play first:\nType 1 if you want to play first.\nType anything except 1 if you want me to play first.")
turn = input()
mode = "hard"
player, bot = False, False
botfirstturn = False
cNum = 0 #current number
if turn == '1':
    player = True
else:
    bot = True
    botfirstturn = True
while True:
    if mode == "hard":
        if player:
            if cNum <= 27:
                print("Choose an number in these 3 numbers: ",cNum+1, ", ", cNum+2,' or ', cNum+3, sep = '')
                cNum = int(input())
            else:
                l = [x for x in range(cNum+1,30+1)]
                print("Choose an number in these",30-cNum,"numbers: ", end = '')
                print(*l, sep = ', ')
                cNum = int(input())
            player = not player
            bot = not bot
        if bot:
            if botfirstturn:
                cNum = 2
                botfirstturn = not botfirstturn
            else:
                cNum = (cNum+3-2)//4*4+2
            print("I(bot) chooses", cNum)
            player = not player
            bot = not bot
        if cNum == 30:
            if player == False:
                print("You win!!!")
            else:
                print("You lose =((")
            break



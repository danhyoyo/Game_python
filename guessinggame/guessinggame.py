import random

number = random.randint(0,101)
print(number)
bot, top = 0, 100
guessing = True
while guessing:
    yourguess = int(input("Guess a number:"))
    if yourguess > number:
        top = yourguess
        print("You guess is bigger than the answer. The number is in range of (", bot, ";", top,')', sep = '')
    elif yourguess < number:
        bot = yourguess
        print("You guess is smaller than the answer. The number is in range of (", bot, ";", top, ')', sep='')
    else:
        print("You have guessed the right answer:", number)
        break

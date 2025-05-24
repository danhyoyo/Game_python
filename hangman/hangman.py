import random
with open('list_of_words.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)

allow_errors = 7
guesses = []
done = False


while not done:
    check = True
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end = ' ')
        else:
            print("_", end = ' ')
    print()
    print("You have", allow_errors, "to guess! Input the letter you guess: ")
    guess = input()
    guesses.append(guess.lower())
    if guess not in word:
        allow_errors -= 1
        if allow_errors == 0:
            break
    for letter in word:
        if letter.lower() not in guesses:
            check = False
    if check:
        done = True
        break
if check:
    print("You won!!! The word is: ", word)
else:
    print("You lose!!! The word is: ", word)
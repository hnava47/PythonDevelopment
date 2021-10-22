import random

secrectNumber = random.randint(1,100)

guess = -10

numberOfGuessesAllowed = 10

print('You have', numberOfGuessesAllowed, 'guesses to figure out my secret number between 1 and 100')
for i in range(numberOfGuessesAllowed):
    guess = int(input("Guess my number?: "))
    if secrectNumber == guess:
        print("You have guessed correctly!")
        break
    else:
        if guess < secrectNumber:
            print("Wrong guess! The number is higher")
        else:
            print("Wrong guess! The number is lower")
else:
    print('You have lost the game!')

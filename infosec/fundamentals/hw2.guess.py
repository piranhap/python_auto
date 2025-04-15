# Refer to Learn/guess.py



# This is a guess the number game, say hi to a user
import random
# print('Hello. What is your name?')
# name = input()
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

# Ask the player up to 6 times

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break

if guess == secretNumber:
    print('Good job you took: ', str(guessesTaken), 'guesses')
else:
    print("I'm sorry!, I was thinking of the number: ", secretNumber)
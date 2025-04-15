# This is a guess the number game, say hi to a user
import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1,10)
print('Well, ' + name + ', I am thinking of a number between 1 and 10')

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
    print('Good job', name, 'you took: ', str(guessesTaken), 'guesses')
else:
    print("I'm sorry!, I was thinking of the number: ", secretNumber)
import random

count = 1
number = random.randrange(101)

print("I'm thinking of a number from 1-100. You have 7 guesses.")
guess = int(input(f"Guess # {count}: "))

while guess != number and count < 7:
    if guess > number:
        print("Sorry, that guess is too high.")
    else:
        print("Sorry, that guess is too low.")

    count += 1
    guess = int(input(f"Guess # {count}: "))

if guess == number:
    print(f"You guessed it! The number was {number}.")
else:
    print(f"Sorry, you didn't guess it in 7 tries. You lose. The number was {number}.")

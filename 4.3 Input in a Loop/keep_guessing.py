number = 4

print("I have chosen a number between 1 and 10. Try to guess it.")
guess = int(input("Your guess: "))

while guess != number:
    print("That is incorrect. Guess again.")
    guess = int(input("Your guess: "))

print(f"That's right! The number was {number}. You're a good guesser.")

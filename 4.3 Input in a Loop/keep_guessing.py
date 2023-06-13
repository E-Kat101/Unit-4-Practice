number = 4

print("I have chosen a number between 1 and 10. Try to guess it.")

while True:
    guess = int(input("Your guess: "))
    if guess == 4:
        print(f"That's right! The number was {number}. You're a good guesser.")
        break

    print("That is incorrect. Guess again.")

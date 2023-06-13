number = 4
count = 0

print("I have chosen a number between 1 and 10. Try to guess it.")

while True:
    guess = int(input("Your guess: "))
    count += 1
    if guess == 4:
        print(f"That's right! The number was {number}. You're a good guesser.")
        print(f"That only took you {count} tries.")
        break

    print("That is incorrect. Guess again.")

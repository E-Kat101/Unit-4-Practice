# 1. Change the code so that it locks them out after 4 tries instead of 3. Make sure to change the condition at the bottom, too.
# 2. Make a variable (constant) for the number of maximum tries allowed. Use that variable everywhere instead of just the number.
PIN = "12345"
tries = 0
max_tries = 4

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < max_tries:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
    tries += 1

if entry == PIN:
    print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= max_tries:
    print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")

"""
1. How is a while loop similar to an if statement?
A while loop is similar to an if statement as they both run code only when the statement is true.

2. How is a while loop different from an if statement?
A while loop is different from an if statement because an if statement only runs once, whereas a while loop is a loop, and runs as long as the statement is true.

3. What would we have to change in our program if the PIN was stored as an integer rather than a string? For example if it was initialized as PIN = 12345.
We would have to surround the input function with an int() to convert whatever the user inputs into an integer.
"""
PIN = 12345
print("WELCOME TO THE BANK OF GALLO.")
entry = int(input("ENTER YOUR PIN: "))

while entry != PIN:
    print("\nINCORRECT PIN. TRY AGAIN.")
    entry = int(input("ENTER YOUR PIN: "))

print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")

"""
4. Comment out the line entry = input(...) from inside the while loop. What happens? Why?
If the user inputs an incorrect pin, the text "INCORRECT PIN. TRY AGAIN" will be pasted an infinite amount of times. This is because the user does not get another chance to input a different pin, so the entry stays as a value that is not equal to the correct value, and the statement comes out as true. Thus, the loop runs forever.
"""

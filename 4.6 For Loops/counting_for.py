"""
1. What happens when you change the loop variable n to some other name?(Then change it back.) Why do you suppose I chose to name this particular loop variable “n”?
When you change the loop variable n to some other name, you have to also change the variable name in the print statement. Otherwise, nothing changes. I suppose that you chose to name this particular loop variable "n" because n typically stands for "number", and this code is meant to print the user's input a certain number of times.

2. How do the first two arguments (0, 5) given to the range function effect the loop? Change them and experiment. Change it back.
The first argument given is the integer that the loop starts at, and this integer is included. On the other hand, the second argument given is the integer that the loop ends on, but this integer is excluded.

3. What do you suppose the third number given to the range function is for? Change it to 2 and see. Change it back.
The third number given to the range function states what the numbers in the loop skip by.

4. What happens when you call the range function with only one number? i.e. range(7)?
The loop starts from 0 and goes up until 6 (including 6), so in total, the number of times the message is printed is seven, but the actual number "7" is not included in the output.

5. What happens when you call the range function with only two numbers? i.e. range(3, 9)?
The loop starts at the first number and goes up until, but not including, the second, going up by one.
"""
# 6. Change the code so that the loop repeats ten times instead of five.
print("Type in a message, and I'll display it ten times.")

message = input("Message: ")

for n in range(0, 10, 1):
    print(f"{n}. {message}")

# 7. See if you can change the for loop so that the message starts at 2 and counts by twos
print("Type in a message, and I'll display it ten times.")

message = input("Message: ")

for n in range(2, 21, 2):
    print(f"{n}. {message}")

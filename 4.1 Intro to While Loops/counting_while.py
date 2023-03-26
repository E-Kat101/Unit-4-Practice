# 1. n += 1 increases the count by 1. Without it, the count will always equal the original value that was assigned to n (in this case 0), so the while loop will repeat infinitely because 0 is less than the predetermined value.

# 2. Change the code so that the loop repeats ten times instead of five.
print("Type in a message, and I'll display it ten times.")
message = input("Message: ")

n = 0
while n < 10:
    print(f"{n + 1}. {message}")
    n += 1

# 3. See if you can change the code so that the message still prints ten times, but the number in front count by tens.
print("Type in a message, and I'll display it ten times.")
message = input("Message: ")

n = 0
while n < 100:
    print(f"{n + 10}. {message}")
    n += 10

# 4. Change the code so that it asks the person how many times to display the message. Then, print it that many times. Still count by tens.
print("Type in a message, and I'll display it several times.")
message = input("Message: ")
times = int(input("How many times would you like to display the message? "))

print()

count = 0
while count < times:
    print(f"{(count+1)*10}. {message}")
    count += 1

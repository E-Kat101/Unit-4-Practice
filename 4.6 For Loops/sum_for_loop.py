sum = 0
num = int(input("Enter a number to count up to: "))

for n in range(1, num+1):
    print(n)
    sum += n

print(f"The sum is {sum}.")

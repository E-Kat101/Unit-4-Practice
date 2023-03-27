start = int(input("Count from: "))
end = int(input("Count to: "))
increment = int(input("Count by: "))

for n in range(start, end+1, increment):
    print(n, end = " ")

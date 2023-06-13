total = 0

print("I will add up the numbers you give me.")

while True:
    num = int(input("Number: "))
    if num == 0:
        break
        
    total += num
    print(f"The total so far is {total}.")
    
print(f"The total is {total}.")

# Create a while loop that will:

# 1. calculate the sum of the numbers from 1 to 10.
count = 1
total = 0

while count <= 10:
    total += count
    count += 1

print(total)

# 2. calculate the sum of the numbers from 100 to 200.
count = 100
total = 0

while count <= 200:
    total += count
    count += 1

print(total)

# 3. calculate the difference between the sum of the numbers from 100 to 200 and the sum of the numbers from 200 to 300.
total_1 = 0
total_2 = 0

count_1 = 100
count_2 = 200

while count_1 <= 200 and count_2 <= 300:
    total_1 += count_1
    count_1 += 1

    total_2 += count_2
    count_2 += 1

difference = total_2 - total_1
print(f"The difference between the sum of the numbers from 100 to 200 and the sum of the numbers from 200 to 300 is {difference}.")

# 4. calculate the sum of the multiples of 5 between the numbers 1000 and 10000.
total = 0
count = 1000

while count <= 10000:
    total += count
    count += 5

print(total)

# 5. calculate the sum of the multiples of 5 between 1 and 100, but do not include numbers that are multiples of 3. Modulus (%) will come in handy here.
sum = 0
count = 0

while count <= 100:
    count += 5
    if count%5 == 0 and count%3 != 0:
        sum += count

print(sum)

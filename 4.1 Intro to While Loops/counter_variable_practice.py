"""
Create a loop that will count from:

1. 0 to 10 by 1.
2. 10 to 0 by 1.
3. from 491 to 586 by 5.
4. from 124 to 810 by 14.
5. from -233 to -113 by 4.
6. from 215 to 300 by 5.
7. from -310 to -94 by 8.
8. from -476 to -410 by 3.
9. from -327 to -147 by 9.
10. from 484 to 1024 by 18.
"""
# 1.
count = 0
while count <= 10:
    print(count)
    count += 1

# 2.
count = 10
while count >= 0:
    print(count)
    count -= 1

# 3.
count = 491
while count <= 586:
    print(count)
    count += 5

# 4.
count = 124
while count <= 810:
    print(count)
    count += 14

# 5.
count = -233
while count <= -113:
    print(count)
    count += 4

# 6.
n = 215
while n <= 300:
    print(n)
    n += 5

# 7.
n = -310
while n <= -94:
    print(n)
    n += 8

# 8. 
n = -476
while n <= -410:
    print(n)
    n += 3

# 9.
n = -327
while n <= -147:
    print(n)
    n += 9

# 10.
n = 484
while n <= 1024:
    print(n)
    n += 18

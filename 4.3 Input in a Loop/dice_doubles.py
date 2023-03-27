import random

print("HERE COMES THE DICE!")
print()
double = False

while double == False:
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)
    total = dice_1 + dice_2
    
    print(f"Roll #1: {dice_1}")
    print(f"Roll #2: {dice_2}")
    print(f"The total is {total}!")
    print()

    if dice_1 == dice_2:
        double = True

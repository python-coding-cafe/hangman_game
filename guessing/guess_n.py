import random

number = random.randint(1, 10)

while True:
    n = int(input("Enter a number from 1 - 10: "))
    if n < number:
        print("Your number is smaller than the correct number")
    elif n > number:
        print("Your number is Higher than the correct number")
    else:
        print("You Nailed it.")
        end = input("Type 'yes' to continue, or 'no' to quit: ")
        if end == "yes".lower() or end == 'y'.lower():
            continue
        else:
            break

import random
import time

def displayIntro():
    print("You are in a land full of dragons. In front of you,")
    print("you see two caves. In one cave, the dragon is friendly,")
    print("and will share his treasure with you. The other dragon")
    print("is greedy and hungry, and will eat you on sight.")
    print()

def chooseCave():
    cave = ""
    while cave != "1" and cave != "2":
        print("Which cave will you go into? (1 or 2 ?)")
        cave = input()

    return cave

def checkCave(chosenCave):
    print("You approach the cave ... ")
    time.sleep(2)
    print("It is dark and spooky ... ")
    time.sleep(2)
    print("A larg dragon jumps out in front of you! He opens his jaws and ... ")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1 , 2)
    if chosenCave == str(friendlyCave):
        print("Give you his treasure!")
    else:
        print("Gobbles you down in one bite! ")
        print("... 😭")

playAgian = "yes"

while playAgian == "yes" or playAgian == "y":
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print("Do you want to play again? (yes or no)" )
    playAgian = input()

import random
import time
from rich.progress import track


def main():
    guess_num()


def guess_num():
    for i in track(range(10), description="Game is Starting"):
        time.sleep(0.10)

    words = "Welcome to the Number Guessing Game"
    for word in words:
        print(word, end="", flush=True)
        time.sleep(0.10)
    print()

    secret_num = random.randint(1, 9)
    attempts = 0
    max_attempts = 3
    play_again = False
    while attempts < max_attempts and not play_again:
        guess = int(input("Enter a Number between [1 - 9]: "))
        attempts += 1

        if guess < secret_num:
            print("Your Number is [Low]")
            
        elif guess > secret_num:
            print("Your number is [High]")
        else:
            print(f"Good Job 🥰, you nailed the number after {attempts} attempts")

            replay = input("Do you want to play again? [y/n]: ")
            if replay.lower() == "y":
                guess_num()
            else:
                print("Thanks for playing 😊")

            break
    else:
        print("Sorry 😢, You ran out of attempts")
        print(f"The number was {secret_num}")


if __name__ == "__main__":
    main()

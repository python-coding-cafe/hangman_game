import random

def welcome_message():
    print("""
    Welcome to the Coin Guessing game!
    Choose a method to toss the coin:
    1. Using random.random()
    2. Using random.randint()
    """)

def get_user_choice():
    return input("Enter your choice (1 or 2): ")

def toss_coin(choice):
    if choice == "1":
        return 'heads' if random.random() < 0.5 else 'tails'
    elif choice == "2":
        return 'heads' if random.randint(0, 1) == 0 else 'tails'
    else:
        print('Not understood')
        return None

def get_user_guess():
    return input("Enter your guess (Heads or Tails): ").lower()

def check_guess(user_guess, coin_result):
    if user_guess == coin_result:
        print(f"Good guess! The computer choice is {coin_result}")
    else:
        print(f"Bad guess! The computer choice is {coin_result}")

def main():
    welcome_message()
    user_choice = get_user_choice()
    coin_result = toss_coin(user_choice)
    if coin_result:
        user_guess = get_user_guess()
        check_guess(user_guess, coin_result)

if __name__ == "__main__":
    main()
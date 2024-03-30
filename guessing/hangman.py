import random
import json


# Load words from JSON file
with open("words.json") as f:
    words_data = json.load(f)

# Filter for words with definitions
filtered_words = [word_data for word_data in words_data if "definition" in word_data]

if not filtered_words:
    print("No words with definitions found in 'words.json'.")
    exit()

print('Welcome to Hangman')

secret_word_data = random.choice(filtered_words)
secret_word = secret_word_data["word"]
display_word = ['-'] * len(secret_word)

# Access the definition using the secret_word_data dictionary
definition = secret_word_data["definition"]
print(f"Definition: {definition}")

print(display_word)

game_over = False
max_attempts = 7
attempts_left = max_attempts
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

while not game_over:
    guess = input('Guess a letter: ').lower()
    print(f"Definition: {definition}")

    found = False
    for position in range(len(secret_word)):
        if secret_word[position] == guess:
            display_word[position] = guess
            found = True

    if not found:
        attempts_left -= 1
        print(f'You have {attempts_left} attempts left')
        print(hangman[max_attempts - attempts_left -1])

    print(' '.join(display_word))

    if '-' not in display_word:
        # print in green
        print(f'\033[32mCongratulations! 🥰 The word is: {secret_word}\033[0m')
        # print(f'Congratulations! 🥰 The word is: {secret_word}')
        game_over = True

    if attempts_left == 0:
        # print in red
        print(f'\033[31mYou ran out of attempts! You lose! 😢\033[0m')
        # print('You ran out of attempts! You lose! 😢')
        print(f'The word was: {secret_word}')
        game_over = True


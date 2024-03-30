import random
import nltk
from nltk.corpus import words, wordnet

# nltk.download('words')
# nltk.download('wordnet')

word_list = words.words()

# Filter for simple words:
simple_words = [word for word in word_list if len(word) <= 7 and word.isalpha()]

# Filter for words with definitions:
filtered_words = []
for word in simple_words:
    synsets = wordnet.synsets(word)
    if synsets:
        filtered_words.append(word)

if not filtered_words:
    print("No simple words with definitions found. Please check your WordNet installation.")
    exit()

print('Welcome to Hangman')

secret_word = random.choice(filtered_words)
display_word = ['-'] * len(secret_word)

synsets = wordnet.synsets(secret_word)
definition = synsets[0].definition()
print(f"Definition: {definition}")

print(display_word)

game_over = False
max_attempts = 7
attempts_left = max_attempts

while not game_over:
    guess = input('Guess a letter: ').lower()

    found = False
    for position in range(len(secret_word)):
        if secret_word[position] == guess:
            display_word[position] = guess
            found = True

    if not found:
        attempts_left -= 1
        print(f'You have {attempts_left} attempts left')

    print(' '.join(display_word))

    if '-' not in display_word:
        print(f'Congratulations! The word is: {secret_word}')
        game_over = True

    if attempts_left == 0:
        print('You ran out of attempts!')
        print(f'The word was: {secret_word}')
        game_over = True

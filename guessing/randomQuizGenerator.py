# Creates 35 different quizzes.
# Creates 50 multiple-choice questions for each quiz, in random order.
# Provides the correct answer and three random wrong answers for each question, in random order.
# Writes the quizzes to 35 text files.
# Writes the answer keys to 35 text files.
''' the code will need to do the following:
• Store the states and their capitals in a dictionary.
• Call open(), write(), and close() for the quiz and answer key text files.
• Use random.shuffle() to randomize the order of the questions and
multiple- choice options.'''

import random
import csv
import json
countries = 'countries.csv'
data = []

with open(countries, 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        data.append(row)

with open('countries.json', 'w') as json_file:
    json.dump(data, json_file)

print("JSON file has been created.")
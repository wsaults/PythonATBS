#! python3
# A really awesome magic 8 ball script that Zander wrote!

import random

answers = [
  'Ask again later',
  'Yes',
  'No',
  'Without a doubt',
  'I have seen it to be true',
  'i do not know'
]

print('Good morning! What is your question!?')
input()

response = answers[random.randint(0, len(answers) - 1)]

print(response)
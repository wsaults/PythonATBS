#! python3
# This is a really cool magic 8 ball script that Isaac wrote!

import random

answers = [
  'Without a doubt',
  'Yes',
  'concentrate and ask again later',
  'No'
]

# def askQuestion():
# askQuestion()

print('what\'s your name?')
name = input()
print('Hello', name, 'what is your question?')
input()

response = answers[random.randint(0, len(answers) - 1)]

print(response)

#!/usr/bin/env python3

import random
import time

messages = ['It is certain',
  'It is decidedly so.',
  'Yes definitely.',
  'Reply hazy try again.',
  'Ask again later.',
  'Concentrate and ask again.',
  'My reply is no.',
  'Outlook not so good.',
  'Very doubtful.']

firstResponses = ['hmmm...',
  'ERm...',
  'Uhh...',
  '......',
  'Thinking...',
  'Oh, uh...']

def askQuestion():
  print('What is your question?')
  input()
  print(firstResponses[random.randint(0, len(firstResponses) - 1)])
  time.sleep(0.5)
  print('...')
  time.sleep(0.25)
  print('...')
  time.sleep(0.3)
  print(messages[random.randint(0, len(messages) - 1)])
  time.sleep(0.5)
  print('Ask me something else? y/n')
  askAgain = input()
  if (askAgain == 'y'):
    askQuestion()
  else:
    print('Ok, may the odds be ever in your favor. Goodbye.')

print("=================================================")
print("Hello, you have awoken me. Don't keep me waiting.")
askQuestion()
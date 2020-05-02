#! python3

import os, shelve

# OS agnostic path creator
print(os.path.join('usr','bin','spam'))

# get current working directory
print(os.getcwd())

# change directory
# os.chdir('/Users/')
# print(os.getcwd())

# create new directory
# os.makedirs('/Users/exampleDir')

# open a file
sampleFile = open('./sampleFile.txt')
print(sampleFile.read())
sampleFile.close()

# open file with overrite mode
# open('file.txt', 'w')

# open file with append mode
# open('file.txt', 'a')


# shelf files can be stored and opened the next time
# the script runs

# shelfFile = shelve.open('mydata')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelfFile['cats'] = cats
# shelfFile.close()

# pretty print
# pprint.pformat(cats)
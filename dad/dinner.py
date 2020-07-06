#! python3

import random
import time

meals = [
  'Chicken Stew',
  'Meat Sauce Spagetti',
  'Roast',
  'Egg / Bacon Breakfast',
  'Chicen Fettuccine alfredo',
  'Mash potato cassarole',
  'Red beans and rice',
  'White beans and rice',
  'Pork chops and gravy',
  'Lasagna',
  'Salisbury steak',
  'Stromboli',
  'Beef stew',
  'Nuggets and mac',
  'Stroganoff',
  'Burgers',
  'Vegatable Soup',
  'Tacos',
  'Burrito lasanga',
  'Chili',
  'Hamburger helper',
  ]

createdMealLists = []
selectedMealList = []

def createList():
  upComingMeals = set([])
  while len(upComingMeals) < 5:
    meal = meals[random.randint(0, len(meals) - 1)]
    upComingMeals.add(meal)

  for meal in upComingMeals:
    print(meal)

  createdMealLists.append(upComingMeals)

  time.sleep(0.5)

  print('...')
  print('Would you like me to create a new list? y/n')
  goAgain = input()
  if (goAgain == 'y'):
    createList()

def mealPlanner():
  print('Here\'s your meals for this week.')
  time.sleep(0.5)
  print('...')

  createList()

  print('Here\'s the lists you made. Choose a number? 1...' + str(len(createdMealLists)))
  for index, meal in enumerate(createdMealLists):
    print(index, meal)

  chosenIndex = input()
  mealList = createdMealLists[int(chosenIndex)]

  print('You chose:')
  print("============================")
  for meal in mealList:
    print(meal)
  print("============================")
  print('Shall I text these to you? y/n')
  sendText = input()
  if (sendText == 'y'):
    # send it
    print('Ok, I\'ll text you.')

print("============================")
print("Hello, time to make the list!.")
mealPlanner()
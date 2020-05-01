#!/usr/bin/python

# Tic-Tac-Toe

def newBoard():
  return {  'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
  print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
  print('-+-+-')
  print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
  print('-+-+-')
  print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def play():
  theBoard = newBoard()
  turn = 'X'
  turnNumber = 0
  
  while turnNumber < 9:
    print('==== Turn #{} ===='.format(turnNumber + 1))
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()

    # Check if the move is valid
    if move in theBoard:
      # Only set the move if the spot is free
      if theBoard[move] == ' ':
        theBoard[move] = turn
        turnNumber += 1
      else:
        print('That spot has already been taken. Choose another spot.')
        continue
    else:
      print("That isn't a valid spot. Type something like 'mid-M'.")
      
    if turn == 'X':
      turn = 'O'
    else:
      turn = 'X'

  printBoard(theBoard)
  print('Play again? y/n')
  playAgain = input()
  if playAgain == 'y':
    play()
  else:
    print('Bye!')

play()
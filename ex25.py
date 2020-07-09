
import random

def generateNumber(minNum, maxNum):

  num = random.randint(minNum, maxNum)
  return num

def identifyNumber():

  global lowLimit, highLimit, guessCount

  guessCount = 0
  lowLimit = 0
  highLimit = 100
  num = generateNumber(lowLimit, highLimit)

  while True:

    usrComment = input(f"Is your number {num}? If yes press 'y' or 'q' to quit. \nIf not please comment is your number high(type: h) or low(type: l) than the guessed number: ")

    if usrComment == 'q':
      break
    if usrComment == 'y':
      print(" Hurray !!!")
      print(f" Guess count: {guessCount - 1}")
      break
    if usrComment == 'h':
        lowLimit = num + 1
    if usrComment == 'l':
        highLimit = num -1
    guessCount += 1
    num = generateNumber(lowLimit, highLimit)

identifyNumber()

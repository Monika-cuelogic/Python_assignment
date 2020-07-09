import random

def getNumber():

  numList = list()
  cnt = 0
  while True:
    if cnt == 4:
      break

    val = input(" Enter the value: ")
    if val == "exit" or val == "quit":
      break
    cnt += 1
    numList.append(int(val))
  return numList


def generateRandom():

  num = random.sample(range(0,9), 4)
  return num

def checkCounts():

  global guessCount

  guessCount = 0
  while True:
    choice = input(" Press any key to continue except 'exit' or 'quit' : ")
    if choice == "exit" or choice == "quit":
      break

    usrInput = getNumber()
    randomNum = generateRandom()
    guessCount += 1

    i = 0
    cows = 0
    bulls = 0

    print(f"Generate Random: {randomNum}")
    print(f"User Input num : {usrInput}")

    while i < len(usrInput):

      if usrInput[i] == randomNum[i]:
        cows += 1
        usrInput.remove(usrInput[i])
        randomNum.remove(randomNum[i])

      if usrInput[i] in randomNum:
        bulls += 1
      i += 1

    print(f"Cows: {cows}")
    print(f"Bulls: {bulls}")


checkCounts()
print(f"Guesscount: {guessCount}")

playChance = 0

def putToken(playerToken):

  row = int(input(f" Select row [1, 2, 3] to put token {playerToken}: "))
  column = int(input(f" Select column [1, 2, 3] to put token {playerToken}: "))

  global playChance

  playChance += 1
  row -= 1
  column -= 1
  temp = list(gameList[row])

  if int(temp[column]) == 0:
    temp[column] = playerToken
    gameList[row] = temp
    showGame()
    if checkSequence(playerToken, temp):
      return True
    elif checkColumn(playerToken, column):
      return True
    elif checkDiagonalOne(playerToken):
      return True
    elif checkDiagonalTwo(playerToken):
      return True
    else:
      return False
  else:
    print(" Invalid input!")
    putToken(playerToken)

def checkDiagonalOne(playerToken):

  res = all(i[gameList.index(i)] == playerToken for i in gameList)
  return res

def checkDiagonalTwo(playerToken):
  cnt = 0
  res = True
  for i in gameList:
    if i[(len(i) - 1) - cnt] == playerToken:
      cnt += 1
    else:
      res = False
  return res

def checkColumn(playerToken, column):

  res = all(i[column] == playerToken for i in gameList)
  return res

def checkSequence(playerToken, row):

  res = all(i == playerToken  for i in row)
  return res


def generateGame():

  global gameList

  gameList = list()

  for i in range(0,3):
    temp = list()
    for j in range(0,3):
      temp.append('0')
    gameList.append(temp)

  return gameList


def showGame():
  for i in gameList:
    print(f"{i}\n")


def playGame():

  generateGame()
  showGame()
  global playChance

  playChance = 0
  while True:

    if playChance > 7:
      print("Game Over!!!")
      break

    player1 = putToken('x')
    if player1:
      print(" Player 1 Won !!!!!!")
      break
    player2 = putToken('o')
    if player2:
      print(" Player 2 Won !!!!!!")
      break

playGame()

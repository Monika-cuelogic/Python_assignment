
def putToken(playerToken):

  row = int(input(f" Select row [1, 2, 3] to put token {playerToken}: "))
  column = int(input(f" Select column [1, 2, 3] to put token {playerToken}: "))

  row -= 1
  column -= 1
  temp = list(gameList[row])

  if int(temp[column]) == 0:
    temp[column] = playerToken
    gameList[row] = temp
    showGame()
    if checkSequence(playerToken, temp):
      return True
    if checkColumn(playerToken, column):
      return True
    if checkDiagonal(playerToken):
      return True
  else:
    print(" Invalid input!")
    putToken(playerToken)

def checkDiagonal(playerToken):

  res = all(i[gameList.index(i)] == playerToken for i in gameList)
  if res:
    return res

  res = all(i[(len(i) - 1) - gameList.index(i)] == playerToken for i in gameList)
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
      temp.append(0)
    gameList.append(temp)

  return gameList


def showGame():
  for i in gameList:
    print(f"{i}\n")


def playGame():

  generateGame()
  showGame()

  while True:

    player1 = putToken(1)
    if player1:
      print(" Player 1 Won !!!!!!")
      break
    player2 = putToken(2)
    if player2:
      print(" Player 2 Won !!!!!!")
      break

playGame()
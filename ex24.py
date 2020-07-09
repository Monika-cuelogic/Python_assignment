def printHorizontal(lines, times):

  for i in range(times):
    print("  ", end='')
    for j in range(lines):
      print("-", end='')
    print(" ", end='')
  print("")

def printVertical(lines, times):

  verSpaces = lines + 2
  verTimes = times + 1

  for i in range(verTimes):
    print("|", end='')
    for j in range(verSpaces):
      print(" ", end='')
  print("")


def drawGame(lines, times):

  count = 0

  while count < lines:
    count += 1
    printHorizontal(lines, times)
    printVertical(lines, times)
  printHorizontal(lines, times)

lines = int(input(" Enter number of blocks to Print: "))
times = lines

drawGame(lines, times)
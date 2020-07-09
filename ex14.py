
def createList():

  exList = list()

  print(" Enter 'q' to quit ")

  while True:

    userInput = input(" Enter the numbers: ")
    if userInput == "q":
      break
    exList.append(int(userInput))

  return exList

def getFormattedList():

  usrList = set(createList())
  print(f" The Formatted user input without duplicated values are: {usrList}")


getFormattedList()
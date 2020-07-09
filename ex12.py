
def formatList():

  num = list()
  newList = list()
  print(" Enter 'quit' or 'exit' for halting")

  while True:
    data = input(" Enter the number list: ")

    if data == "exit" or data == "quit":
      break

    num.append(data)

  newList.append(int(num[0]))
  newList.append(int(num[len(num)-1]))
  print(f" New list with first and last element are: {newList}")

formatList()
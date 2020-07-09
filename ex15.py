def printReverse(usrInput):

  newString = " "

  inputList = usrInput.split(" ")
  newString = newString.join(inputList[::-1])

  return newString


usrInput = input(" Enter your string: ")
newString = printReverse(usrInput)
print(f" This is reversed string: \n {newString}")
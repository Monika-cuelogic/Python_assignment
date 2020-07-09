
def binSearch(numList, num):

  mid = 0

  if num >= numList[0] and num <= numList[ len(numList) - 1 ]:

    mid = int(len(numList)/2)

    if numList[mid] == num:
      print("True")

    elif num > numList[mid]:
      binSearch(list(numList[mid:]), num)
    else:
      binSearch(list(numList[:mid]), num)

  else:
    print("False")


def getNumber():

  totalNum = int(input(" Enter the total count: "))

  global numList
  numList = list()
  cnt = 0
  prev = -1
  while True:
    if cnt == totalNum:
      break

    val = input(" Enter the value: ")
    if val == "exit" or val == "quit":
      break

    if prev < int(val):
      cnt += 1
      numList.append(int(val))
      prev = int(val)
    else:
      print(" Value is greater than or equal to prev number")

  return numList

numList = getNumber()
num = int(input(" Enter the number to search: "))
binSearch(numList, num)
import random

def getRandom():

  fp = open("sowpods.txt")
  randomWord = ""

  data = fp.read()
  dataList = data.split("\n")

  randomList = random.sample(dataList, k=1)
  print(f" Random word from list is: {randomWord.join(randomList)}")

getRandom()
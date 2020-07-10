import random

def getRandom():

  fp = open("sowpods.txt")
  randomWord = ""

  data = fp.read()
  dataList = data.split("\n")

  randomList = random.sample(dataList, k=1)
  # return randomList
  return randomWord.join(randomList)



def initGame():

  print("Welcome to Hangman!")

  global randomWord
  global newWord

  newWord = list()
  randomWord = getRandom()

  wordLength = len(randomWord)

  for i in range(wordLength):
    print("_ ", end='')
    newWord.append("_ ")
  print("\n")

def populateLetterInWord(letter):

  global randomWord
  global newWord

  cnt = 0

  for i in randomWord:
    if i == letter:
      newWord[cnt] = letter
    cnt += 1

  print("".join(newWord))


def playGame():

  initGame()
  global newWord
  global randomWord
  global guessList
  guessList = set()

  totalAttempts = 6
  while True:

    if len(guessList) < 6:
      letter = input(" Guess the letter in word: ").upper()
      guessList.add(letter)
      populateLetterInWord(letter)
      print(f"{totalAttempts - len(guessList)} Attempts Left!")
    else:
      break

    if(letter == "QUIT"):
      break


playGame()
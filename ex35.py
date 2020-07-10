import json
from collections import Counter

def dataInitialize():

  fp = open('data.json',)
  dataDic = json.load(fp)
  return dataDic

def getBirthdays():

  birthDic = dataInitialize()
  print("We know the birthdays of:")
  for i in birthDic['birthDetails']:
    print(f"{i}")

  name = input(" Who's birthday do you want to look up? ")
  print(f" {name}'s birthday is: {birthDic['birthDetails'][name]}")


def writeFile(data):
  with open("data.json", 'w') as f:
    json.dump( data ,f,indent=4)

  print("Birthday added !!!")

def addBirthdays(name, birthDate):

  newData = {}

  data = dataInitialize()
  exData = data['birthDetails']
  exData[name] = birthDate
  newData['birthDetails'] = exData
  writeFile(newData)

def getMonthwiseCount():

  data = dataInitialize()

  months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  exData = [ months[int(i.split('/')[1]) - 1] for i in data['birthDetails'].values()]
  res = Counter(exData)

  print(f" \nMonthwise count: {res}\n")

def chooseOption():

  while True:
    print(" Enter 'q' OR 'e' to quit:")
    option = input("Do you want to add birthday enter 'a' OR to display enter 'd' \n To get monthwise birthday count enter 'm': ")
    if option == 'q' or option == 'e':
      break

    if option == 'a':
      name = input("Enter name: ")
      birthday = input(" Enter birthday: ")
      addBirthdays(name, birthday)
    elif option == 'd':
      getBirthdays()
    elif option == 'm':
      getMonthwiseCount()
    else:
      print("Invalid input !!!")

chooseOption()
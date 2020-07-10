import json


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

def chooseOption():

  while True:
    print(" Enter 'q' OR 'e' to quit:")
    option = input("Do you want to add birthday enter 'a' OR to display enter 'd': ")
    if option == 'q' or option == 'e':
      break

    if option == 'a':
      name = input("Enter name: ")
      birthday = input(" Enter birthday: ")
      addBirthdays(name, birthday)
    elif option == 'd':
      getBirthdays()
    else:
      print("Invalid input !!!")

chooseOption()
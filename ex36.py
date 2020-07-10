import json
from collections import Counter
from bokeh.io import output_file, show
from bokeh.plotting import figure

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

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

  global months

  data = dataInitialize()

  exData = [ months[int(i.split('/')[1]) - 1] for i in data['birthDetails'].values()]
  res = Counter(exData)

  return res


def getHistogram():

  global months

  res = getMonthwiseCount()
  categoriesList = list()
  countList = list()

  output_file("birthdayDate.html")

  newRes = [res[i] if i in res else 0 for i in months ]

  p = figure(x_range=months, plot_height=250, title="Birthday Month Counts", toolbar_location=None, tools="")

  p.vbar(x=months, top=newRes, width=0.9)

  p.xgrid.grid_line_color = None
  p.y_range.start = 0

  show(p)

def chooseOption():

  while True:
    print(" Enter 'q' OR 'e' to quit:")
    option = input("1. To add birthday enter 'a' \n 2. To display enter 'd' \n 3. To get monthwise birthday count enter 'm' \n 4. To plot histogram enter 'h': ")
    if option == 'q' or option == 'e':
      break

    if option == 'a':
      name = input("Enter name: ")
      birthday = input(" Enter birthday: ")
      addBirthdays(name, birthday)
    elif option == 'd':
      getBirthdays()
    elif option == 'm':
      print(f" \nMonthwise count: {getMonthwiseCount()}\n")
    elif option == 'h':
      getHistogram()
    else:
      print("Invalid input !!!")

chooseOption()

def dataInitialize():

  dataDic = {"a": "12/12/1990", "b": "1/12/1991", "c": "15/12/1990", "d": "12/11/1990", "e": "1/1/1992"}
  return dataDic

def getBirthdays():

  birthDic = dataInitialize()
  print("Welcome to the birthday dictionary. We know the birthdays of:")
  for i in birthDic:
    print(f"{i}\n")

  name = input(" Who's birthday do you want to look up? ")
  print(f" {name}'s birthday is: {birthDic[name]}")

getBirthdays()
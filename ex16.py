import random

passStr = ""

def generateWeak():
  passWeak = random.sample('abcdefghijklmnopqrstuvwxyz', 5)
  return passStr.join(passWeak)

def generateStrong():
  passAlpha = random.sample('abcdefghijklmnopqrstuvwxyz', 3)
  passNumber = random.sample('0123456789', 3)
  passSpecial = random.sample('!@#$%^&*_+|":?></-=', 3)
  passStrongList = passSpecial + passNumber + passAlpha
  return passStr.join(passStrongList)

def generateNormal():
  passAlpha = random.sample('abcdefghijklmnopqrstuvwxyz', 5)
  passNumber = random.sample('0123456789', 3)
  passNormalList = passNumber + passAlpha
  return passStr.join(passNormalList)

def passGenerator(param1):

  if param1 == "weak":
    print(f"{generateWeak()}")

  if param1 == "normal":
    print(f"{generateNormal()}")

  if param1 == "strong":
    print(f"{generateStrong()}")


param = input("Enter your choice:")
passGenerator(param)
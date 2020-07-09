
res = {}

newPrime = open("prime.txt")
newHappy = open("happy.txt")

primeStr = newPrime.read()
happyStr = newHappy.read()

primeList = primeStr.split("\n")
happyList = happyStr.split("\n")

res = [i for i in primeList if i in happyList]

print(f" Overlapping numbers are: {res}")
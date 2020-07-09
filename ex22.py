
res = {}

newFile = open("names.txt")
dataStr = newFile.read()
dataList = dataStr.split("\n")

for i in dataList:
  if i in res:
    temp = res[i]
    res[i] = temp + 1
  else:
    res[i] = 1

print(f"Result: {res}")
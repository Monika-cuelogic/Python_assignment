a = [1, 5, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

res = [i for i in a if i in b]
finList = list()
for i in res:
  if i not in finList:
    finList.append(i)

print(f"{finList}")
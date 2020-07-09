
def fibbo(num):
  i = 1
  prev = 0
  curr = 0
  newList = list()
  count = 0
  while num > count:

    count += 1
    if prev == 0:
      newList.append(i)

    curr = prev + i
    newList.append(curr)
    prev = i
    i = curr

  print(f" Fibonacci series: {newList}")

num = int(input(" Enter the number: "))

fibbo(num)

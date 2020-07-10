
def getNumbers():

  count = 0
  numList = list()
  while count < 3:

    nums = int(input(" Enter the number: "))

    numList.append(nums)

    count += 1

  return numList

def findHighest():

  nums = getNumbers()
  highest = 0

  if nums[0] > nums[1]:
    if nums[0] > nums[2]:
      highest = nums[0]
    else:
      highest = nums[2]
  elif nums[1] > nums[2]:
    highest = nums[1]
  else:
    highest = nums[2]

  print(f"Highest is: {highest}")

findHighest()


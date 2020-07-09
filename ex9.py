import random

guessCount = 0

while True:

  val = input(" Enter the value: ")
  if val == "exit" or val == "quit":
    break

  guessCount += 1
  val = int(val)
  num = random.randint(1,9)

  if num == val:
    print(f"{num}: Your guess is right!")
  elif abs(val-num) <= 2:
    print(f"{num}: You are very close!")
  elif abs(val - num) > 2 and abs(val - num) <= 4:
    print(f"{num}: You can do it")
  else:
    print(f"{num}: Better luck next time")

print(f" Total guess counts are: {guessCount}")
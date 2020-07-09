while True:

  num = input(" Enter a number: ")

  if num == "exit" or num == "quit":
    break

  num = int(num)
  res = [i for i in range(2, num) if num%i == 0 ]

  if len(res) == 0:
    print(f"{num} is Prime")
  else:
    print(f"{num} is Non-prime")

player1 = input(" Enter the option: Player1: ")
player2 = input(" Enter the option: Player2: ")

validData = ["Rock", "Paper", "Scissors"]

if (player1 in validData and player2 in validData):

  if player1 == player2:
    print(" That's a tie")

  elif player1 == "Rock":
    if player2 == "Scissors":
      print("Rock Wins")
    else:
      print("Paper Wins")

  elif player1 == "Scissors":
    if player2 == "Paper":
      print(" Scissors Wins")
    else:
      print("Rock Wins")

  elif player1 == "Paper":
    if player2 == "Rock":
      print("Paper Wins")
    else:
      print("Scissors Wins")
else:
  print("Invalid Input")


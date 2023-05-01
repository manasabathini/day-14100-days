from getpass import getpass as input

print("ROCK, PAPER, and SCISSORS")
print("Please enter 'R' for Rock, 'P' for Paper and 'S' for Scissors")
player_1 = input("Player 1 > Please enter your input to play the game: ")
player_2 = input("Player 2 > Please enter your input to play the game: ")
print()

if player_1 == "R":
  if player_2 == "R":
    print("Both picked Rock, draw")
  elif player_2 == "P":
    print("Player1's Rock is smothered by Player2's Paper!")
  elif player_2 == "S":
    print("Player1 smashed Player2's Scissors into dust with their Rock!")
  else:
    print("Invalid pick player_2!")
elif player_1 == "P":
  if player_2 == "R":
    print("Player2's Rock is smothered by Player1's Paper!")
  elif player_2 == "P":
    print("Two bits of paper flap at each other. Dissapointing. Draw.")
  elif player_2 == "S":
    print("Player1's Paper is cut into tiny pieces by Player2's Scissors!")
  else:
    print("Invalid pick player_2")
elif player_1 == "S":
  if player_2 == "R":
    print("Player 2's Rock makes metal-dust out of Player1's Scissors")
  elif player_2 == "P":
    print("Player1's Scissors make confetti out of Player2's paper!")
  elif player_2 == "S":
    print("Ka-Shing! Scissors bounce off each other like a dodgy sword fight! Draw")
  else:
    print("Invalid pick player_2!")
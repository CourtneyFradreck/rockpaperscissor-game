import random

print("Hi, Welcome!! "
      "Lets Play a Game!!!")

def playgame() -> object:
    Game = ["Rock", "Paper", "Scissors"]
    player = input("Choose Between Rock, Paper or Scissors: ")
    print(f"You Chose {player}")

    computer = random.choice(Game)
    print(f"Computer Chose {computer}")

    if computer == "Rock" and player == "Rock":
        print("Congratulations, Its a Draw!! We Both Chose Rock")

    elif computer == "Rock" and player == "Paper":
        print("Congratulations!! You Won!!")

    elif computer == "Rock" and player == "Scissors":
        print("Got You!! Hah Hah Hah!! I won")

    elif computer == "Paper" and player == "Rock":
        print("Aww, Sorry! I won")

    elif computer == "Paper" and player == "Paper":
        print("Wow!! It's a Draw")

    elif computer == "Paper" and player == "Scissors":
        print("Nice Try!! You Won!! Wanna Go Again?")

    elif computer == "Scissors" and player == "Rock":
        print("Congrats!! You beat me!")

    elif computer == "Scissors" and player == "Paper":
        print("Hah Hah Hah!!! You're a Loser")

    elif computer == "Scissors" and player == "Scissors":
        print("Oh No Its A Draw!!")

    else:
        print("You Chose an Invalid Option...I Won!!")

playgame()

# Put a Funtion To Keep High Scores
loop = input("Do you still wanna play the game? y/n ")
while loop == "y":
    playgame()

from random import randint
t = ("rock", "paper", "scissors", "lizard", "spock")
computer = t[randint(0, 4)]

player = False

while player == False:
    player = input("rock, paper, scissors, lizard, spock, ")
    if player == computer:
        print("Tie")


    
    elif player == "rock":
        if computer == "scissors":
            print("You win", player, "crushes", computer)
        else:
            print("You lose", computer, "covers", player)
    elif player == "rock":
        if computer == "lizard":
            print("You win", player, "crushes", computer)
        else:
            print("You lose", computer, "vaperizes", player)
    elif player == "paper":
        if computer =="spock":
            print("You win", player, "disproves", computer)
        else:
            print("You lose", computer, "cuts", player)
    elif player == "paper":
        if computer == "rock":
            print("You win", player, "covers", computer)
        else:
            print("You lose", computer, "eats", player)
    elif player == "scissors":
        if computer == "paper":
            print("You win", player, "cuts", computer)
        else:
            print("You lose", computer, "crushes", player)
    elif player == "scissors":
        if computer == "lizard":
            print("You win", player, "decapitates", computer)
        else:
            print("You lose", computer, "smashes", player)
    elif player == "lizard":
        if computer == "paper":
            print("You win", player, "eats", computer)
        else:
            print("You lose", computer, "crushes", player)
    elif player == "lizard":
        if computer == "spock":
            print("You win", player, "poisons", computer)
        else:
            print("You lose", computer, "decapiates", player)
    elif player == "spock":
        if computer == "rock":
            print("You win", player, "vaperizes", computer)
        else:
            print("You lose", computer, "disproves", player)
    elif player == "spock":
        if computer == "scissors":
            print("You win", player, "smashes", computer)
        else: 
            print("You lose", computer, "poisons", player)
    else:
        print("That's not a valid play, Check Spelling")   
player = False
computer = t[randint(0, 4)]
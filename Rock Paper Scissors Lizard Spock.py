# Rock Paper Scissors Lizard Spock part 2

from random import randint

t = ("Rock", "Paper", "Scissors", "Lizard", "Spock")
computer = t[randint(0, 4)]

player = False

while player == False:

	player = input("Rock, Paper, Scissors, Lizard, Spock ")
	if player == computer:
		print("Tie")

	# Rock code starts here
	elif player == "Rock":
		if computer == "Paper":
			print("You lose", computer, "covers", player)
		else:
			print("You win", player, "smashes", computer)
	elif player == "Rock":
		if computer == "Scissors":
			print("You win", player, "smashes", computer)
		else:
			print("You lose", computer, "vaperizes", player)
	elif player == "Rock":
		if computer == "Lizard":
			print("You win", player, "crushes", computer)
		else:
			print("You lose", computer, "poisons", player)		
	elif player == "Rock":
		if computer == "Spock":
			print("You lose", computer, "vaperizes", player)
		else:
			 print("You win", player, "poisons", computer)
	
	
	# Paper code starts here
	elif player == "Paper":
		if computer == "Lizard":
			print("You lose", computer, "eats", player)
		else:
			print("You win", player, "decapitates", computer)
	elif player == "Paper":
		if computer == "Spock":
			print("You win", player, "disproves", computer)
		else:
			print("You lose", computer, "Poisons", player)
	elif player == "Paper":
		if computer == "Rock":
			print("You win", player, "covers", computer)
		else:
			print("You lose", computer, "cuts", player)
	elif player == "Paper":
		if computer == "Scissors":
			print("You lose", computer, "cuts", player)
		else:
			print("You win", player, "smashes", computer)

	# Scissors code starts here
	elif player == "Scissors":
		if computer == "Rock":
			 print("You lose", computer, "crushes", player)
		else:
			print("you win", player, "covers", computer)
	elif player == "Scissors":
		if computer == "Paper":
			print("You win", player, "cuts", computer)
		else:
			print("You lose", computer, "crushes, player")            
	elif player =="Scissors":
		if computer == "Lizard":
			print("You win", player, "decapitates", computer)
		else:
			print("You lose", computer, "crushes1", player)
	elif player == "Scissors":
		if computer == "Spock":
			print("You lose", computer, "smashes", player)
		else:
			print("You win", player, "poisons", computer)
	
	# Lizard code starts here
	elif player == "Rock":
		if computer == "lizard":
			print("You win", player, "crushes", computer)
		else:
			print("You lose", computer, "decapitates", player)    
	elif player == "Paper":
		if computer == "Lizard":
			print("You lose", computer, "eats", player)
		else:
			print("You win", player, "crushes", computer)    
	elif player == "Lizard":
		if computer == "Scissors":
			print("You lose", computer, "decapitates", player)
		else:
			print("You win", player, "poisons", computer)    
	elif player == "Lizard":
		if computer == "Spock":
			print("You win", player, "poisons", computer)
		else:
			print("You lose", computer, "decapitates", player)
	 
	 # Spock code starts here
	elif player == "Spock":
		if computer == "Rock":
			print("You win", player, "vaperizes", computer)
		else:
			print("You lose", computer, "disproves", player)
	elif player == "Spock":
		if computer == "Paper":
			print("You lose", computer, "disproves", player)
		else:
			print("You win", player, "eats", computer)
	elif player == "Spock":
		if computer == "Scissors":
			print("You win", player, "smashes", computer)
		else:
			print("You lose", computer, "poiosns", player)
	elif player == "Spock":
		if computer == "Lizard":
			print("You lose", computer, "eats", player)
		else:
			print("You win", player, "crushes", player) 
	else:
		print("That's not a valid play, Check Spelling")   
player = False
computer = t[randint(0, 4)]


	
	
	
	
	
	
	
	



	
	 

	
		




	

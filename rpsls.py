from random import randint

t = ("rock", "paper", "scissors", "lizard", "spock")

computer = t[randint(0, 4)]



player = False



while player == False:

    player = input("rock, paper, scissors, lizard, spock, ")

    if player == computer:

        print("Tie")







    elif player == 'rock':

        if computer == 'Lizard' or computer == 'scissors':

            print ("You Win", player, 'beats', computer)

        else:

            print ("You Lose", computer, 'beats', player)

    elif player == 'scissors':

        if computer == 'paper' or computer == 'lizard':

            print ('You Win', player, 'beats', computer)

        else:

            print ('You Lose', computer, 'beats', player)

    elif player == 'spock':

        if computer == 'scissors' or computer == 'rock':

            print ('You Win', player, 'beats', computer)

        else:

            print ('You Lose', computer, 'beats', player)

    elif player == 'lizard':

        if computer == 'spock' or computer =='paper':

            print ('You Win', player, 'beats', computer)

        else:

            print ('You Lose', computer, 'beats', player)

    elif player == 'paper':

        if computer == 'rock' or computer =='spock':

            print ('You Win', player, 'beats', computer)

        else:

            print ('You Lose', computer, 'beats', player)

    else:

        print("That's not a valid play, Check Spelling") 

player = False

computer = t[randint(0, 4)]

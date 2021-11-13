from random import choices, randint
playerLives = 5
computerLives = 5

    player = input("Choose your weapon: rock, paper or scissors: ")
    print("player chose :" + player)
    choices = ["rock","paper","scissors"]
    computer = choices[randint(0,2)]
    print("computer chose : " + computer)
    if(computer == player):
        print("tie! try again")

    elif (player == "rock"):
        if(computer == "paper"):
            print("you lose !")
            playerLives = playerLives - 1
        else:
            print("you win!")
            computerLives = computerLives - 1

    elif (player == "scissors"):
        if(computer == "rock"):
            print("you lose !")
            playerLives = playerLives - 1
        else: 
            print("you win!") 
            computerLives = computerLives - 1

    elif (player == "paper"):
        if(computer == "scissors"):
            playerLives = playerLives - 1
            print("you lose !")
        else: 
            print("you win!") 
            computerLives = computerLives - 1
        
    print("computer lives" + str(computerLives))
    print("player lives" + str(playerLives))

    if playerLives == 0:
            print("you lost! would you like to play again ?")
            choice = input(" Y / N? ")
            if choice == "n"/"N":
                print("better luck next time!")
                exit()
            else: 
                playerLives = 5
                computerLives = 5
                player = False

    elif computerLives == 0:
            print("you won! would you like to play again ?")
            choice = input(" Y / N? ")
            if choice == "n"/"N":
                print("better luck next time!")
                exit()
            else: 
                playerLives = 5
                computerLives = 5
                player = False
   
    player = False 



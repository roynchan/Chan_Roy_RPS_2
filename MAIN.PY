from random import choices, randint
from gameComponents import winLose, gameVars

while gameVars.player is False: 
    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    print("===============================")
    print("player chose :" + gameVars.player)
    gameVars.computer = gameVars.choices[randint(0,2)]
    print("computer chose : " + gameVars.computer)

    if(gameVars.computer == gameVars.player):
        print("===============================")
        print("* TIE ! TRY AGAIN ")
        print("===============================")

    elif (gameVars.player == "rock"):
        if(gameVars.computer == "paper"):
            print("===============================")
            print("* YOU LOSE !")
            print("===============================")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("===============================")
            print("* YOU WIN !")
            print("===============================")
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "scissors"):
        if(gameVars.computer == "rock"):
            print("===============================")
            print("* YOU LOSE !")
            print("===============================")
            gameVars.playerLives = gameVars.playerLives - 1
        else: 
            print("===============================")
            print("* YOU WIN !") 
            print("===============================")
            gameVars.computerLives = gameVars.computerLives - 1

    elif (gameVars.player == "paper"):
        if(gameVars.computer == "scissors"):
            gameVars.playerLives = gameVars.playerLives - 1
            print("===============================")
            print("* YOU LOSE !")
        else: 
            print("===============================")
            print("* YOU WIN !") 
            print("===============================")
            gameVars.computerLives = gameVars.computerLives - 1
        
    print("---- computer lives: " + str(gameVars.computerLives))
    print("---- player lives: " + str(gameVars.playerLives))
    print("===============================")

    if gameVars.playerLives == 0:
            winLose.winorlose("lost")

    elif gameVars.computerLives == 0:
            winLose.winorlose("won")

   
    gameVars.player = False 



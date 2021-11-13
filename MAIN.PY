from random import choices, randint
playerLives = 5
computerLives = 5
player = False 
while player is False: 
    player = input("Choose your weapon: rock, paper or scissors: ")
    print("player chose :" + player)
    choices = ["rock","paper","scissors"]
    computer = choices[randint(0,2)]
    print("computer chose : " + computer)
   
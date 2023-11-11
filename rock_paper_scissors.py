#Import “Random” library.
import random
  
    
#Assign a random play to the computer from a list of options (rock, paper, or scissors).
options =["rock","paper","scissors"]
comp_result = random.choice(options)


while True:
    
    #Take the input from the player.
    player_input = input("Enter your choice(from rock, paper, scissors):  ")

    #Print an error message to the user if the input is incorrect.
    #Compare the player’s input to the computer’s.
    #Print the game result to the user.
    if player_input == "rock" or player_input == "paper" or player_input == "scissors":
        if player_input == comp_result:
            print(comp_result,", tie!!!!")
        else:
            if player_input == "rock" and comp_result == "paper" :
                print(comp_result,", You Lost!!!!")
            elif player_input == "scissors" and comp_result == "rock":
                print(comp_result,", You Lost!!!!")
            elif player_input == "paper" and comp_result == "scissors":
                print(comp_result,", You Lost!!!!")
            else: 
                print(comp_result,", You Won!!!!")
    else:
        print("Input is incorrect!!!")


    

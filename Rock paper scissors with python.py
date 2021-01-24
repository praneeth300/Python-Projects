#To create a rock,paper and scissor game we need to first take the input from the user and compare it with the computer choice which is taken using the random module in the python from a list of choices

import random

choices=['Rock','Paper','Scissors']
AI=random.choice(choices)
player=False
AI_Score=0
Player_score=0
while True:
    player=input("Rock,Paper or Scissor??").capitalize()
    #Conditions
    if player == AI:
        print('Tie..!')
    elif player == "Rock":
        if AI == "Paper":
            print("You lose!", AI,'cover',player)
            AI_Score+=1
        else:
            print('You win..!',player,'Smashes',AI)
            Player_score+=1
    elif player == "Scissors":
        if AI == "Rock":
            print("You lose.!",AI,'smashes the',player)
            AI_Score+=1
        else:
            print('You win',player,'cuts',AI)
            Player_score+=1
    elif player == "Paper":
        if AI == "Scissors":
            print('You lose..!',AI,'Cuts',player)
            AI_Score+=1
        else:
            print('You win',player,'Covers',AI)
            Player_score+=1
    elif player=='End':
        print('Final scores: ')
        print(f"AI:{AI_Score}")
        print(f"Player:{Player_score}")
        break
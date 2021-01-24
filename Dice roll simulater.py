#The dice roll simulater can be done by randomly choosing integer between the 1,6 for which we can use the random modeule in python

import random

#Range of values of dice
min_value=1
max_value=6

#to loop the rolling through the user input
rolling_again='yes'

while rolling_again=='yes' or rolling_again == 'y':
    print('Rolling the dices....')
    print('The value are :')
    
    #Genrating and printing 1st random integer from 1 to 6
    print(random.randint(min_value,max_value))

    #Genearting and printing 2nd random integer from 1 to 6
    print(random.randint(min_value,max_value))

    #Asking user to again roll the dice
    roll_again=input('Rolling the dice again??')
#The quiz asks the player questions about animals. They have three chances to answer each question.For ebery correct answer the player will score a point , on the end it revelas the final score of the player

#Let's create the quiz game

def checking_gues(guass,answer):
    global score
    still_gaussing=True
    attempt=0
    while still_gaussing and attempt < 3:
        if guass.lower() == answer.lower():
            print('Correct answer')
            score= score + 1
            still_gaussing=False
        else:
            if attempt < 2:
                guass=input('Sorry wrong answer try again')
            attempt = attempt + 1

        if attempt == 3:
            print('The correct answer is',answer)

score=0

print('Guess the answer for the following questions')
guess1=input('Who is the president of india')
checking_gues(guess1,'Ramnad kovind')
guess2=input('Who is the president of USA')
checking_gues(guess2,'Joe biden')
guess3=input('Which is the tallest animal in the world')
checking_gues(guess3,'Giraffie')
guess4=input('Who is the CEO of Microsoft')
checking_gues(guess4,'Sathya nadendla')

print('Your score is ' + str(score))
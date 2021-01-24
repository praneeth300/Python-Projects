##Story generator with python
#Our task is to generate a random story every time the user runs the program. i will first store the part's of the stories in different lines, then the random module select the random part's of the story stored in the different lines

#import the module
import random

where=['A few years ago','Yeterday','Last night','A long time ago','On 20th jan']
who=['Rakesh','Ranjith','Swetha','Praneeth','Suhaas']
meet=['Went to delhi','Gone for a ride with someone else','Reached Goa for visiting','Went to playground','Got an engaged']
happy=['With a full of exitement','Happiley','Sadly']

print(random.choice(where) + ',' + random.choice(who)+' '+ random.choice(meet) + ',' + random.choice(happy))
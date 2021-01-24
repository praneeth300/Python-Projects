
##To create a password using python, we need to create a program that takes the length of the password and genrates a random password of the same length

import random

pass_word=int(input('Enter you password length'))
d="gdiyuagdebjhsdgcubiwseb185238715378USHUIGSBFCBSDIUGBWEHD?>:!@$%&**"

p=" ".join(random.sample(d,pass_word))

print(p)
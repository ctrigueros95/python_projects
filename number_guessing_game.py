# Number Guessing Game

import random

# Have player guess a Number 

pick = int(input("Pick a number between 1 and 10: "))

# have a random number choosen between range 1-10

rand = random.randrange(1,11,1)

# Check if the numbers are the same

if rand == pick:
    
    print ("Congratulations, you picked correctly")

else:
        
    print ("Sorry better luck next time")

continue


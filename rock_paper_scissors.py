import random

print("1. Rock\n2. Paper\n3. Scissors\n0. Exit")
user_input = input("Pick a number? ")

choice = int(user_input)
opp = random.randrange(1,4,1)

print(opp)

if choice == 1 and opp == 3:
    print("Rock beats scissor! Congratulations you won!")
elif choice == 1 and opp == 2:
    print("Paper beats rock! Better luck next time!")
elif choice == 2 and opp == 1:
    print("Paper beats rock! Congratulations you won!")
elif choice == 2 and opp == 3:
    print("Scissor beats paper! Better luck next time!")
elif choice == 3 and opp == 1:
    print("Rock beats scissor! Better luck next time!")
elif choice == 3 and opp == 2:
    print("Scissor beats paper! Congratulations you won!")
elif choice == 0:
    exit()
else:
    print("Try again its a tie!")

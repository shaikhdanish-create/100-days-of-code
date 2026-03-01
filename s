import random

# 0 = rock, 1 = paper, 2 = scissors
computer = random.randint(0, 2)

user = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

if computer == 0:
    print("Computer chose Rock")
elif computer == 1:
    print("Computer chose Paper")
else:
    print("Computer chose Scissors")

# Winning Logic
if user == computer:
    print("It's a Draw!")
elif (user == 0 and computer == 2) or \
     (user == 1 and computer == 0) or \
     (user == 2 and computer == 1):
    print("You Win!")
else:
    print("Computer Wins!")

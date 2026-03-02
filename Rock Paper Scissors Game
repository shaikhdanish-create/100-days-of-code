# random module using here 
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

# logic explaination
The random module is used to let the computer choose a random number between 0 and 2.

0 = Rock

1 = Paper

2 = Scissors

2️⃣ The user enters a number (0, 1, or 2) as their choice.

3️⃣ The program prints what the computer selected.

4️⃣ Then it checks the winning conditions:

If user choice = computer choice → It's a Draw

If:

Rock beats Scissors

Paper beats Rock

Scissors beats Paper
→ User Wins

Otherwise → Computer Wins

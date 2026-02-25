"""
Number Guessing Game (Python)

Simple mini project.
Computer generates a number between 1 and 10.
User guesses the number.
If correct → You win!
If wrong → Shows correct number.
"""

import random

number = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))

if guess == number:
    print("You win!")
else:
    print("Wrong! Number was", number)

"""
🎮 Number Guessing Game (Python)

📌 About Project:
This is a simple Python mini project.
The program generates a random number between 1 and 10,
and the user tries to guess the correct number.

If the guess is correct, the user wins.
If the guess is wrong, the correct number is displayed.

🛠️ Concepts Used:
- random module
- user input
- type casting
- if-else condition

🚀 Future Improvements:
- Add multiple attempts
- Add score system
- Add difficulty levels
"""

# Import random module
import random

# Generate random number between 1 and 10
number = random.randint(1, 10)

# Take user input
guess = int(input("Guess a number between 1 and 10: "))

# Check condition
if guess == number:
    print("Correct! You win!")
else:
    print("Wrong! The number was", number)

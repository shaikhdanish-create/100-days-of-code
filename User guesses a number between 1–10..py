# Importing random module to generate a random number
import random

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Take user input and convert it into integer
guess = int(input("Guess a number between 1 and 10: "))

# Check if user's guess is correct
if guess == number:
    # If guess matches the random number
    print("Correct! You win!")
else:
    # If guess does not match
    print("Wrong! The number was", number)

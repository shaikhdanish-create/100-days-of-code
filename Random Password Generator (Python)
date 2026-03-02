import random

letters = ['a','b','c','d','e','f','g',
           'A','B','C','D','E','F','G']

numbers = ['1','2','3','4','5','6','7']

symbols = ['*','&','%','$','#','@','!']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

password_list = []

# Add letters
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add numbers
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Add symbols
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Shuffle to make password strong
random.shuffle(password_list)

# Convert list to string
password = ""
for char in password_list:
    password += char

print("Your strong password is:", password)

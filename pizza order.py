print("Welcome to Python Pizza Deliveries!")

size = input("What is your pizza size? S, M or L: ")
pepperoni = input("Do you want extra pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

# Pizza size bill
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
else:
    print("You typed wrong input.")

# Pepperoni bill
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

# Extra cheese bill
if extra_cheese == "y":
    bill += 1
print(f"Your final bill is: ${bill}.")
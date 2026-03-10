from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        is_on = False

    elif choice == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


#description
Displays available coffee options from the menu

Checks if ingredients are sufficient

Handles payment from the user

Prepares the coffee if payment is successful

Shows a report of resources and money

Turns off the machine when requested

This project is useful for learning Object-Oriented Programming (OOP) in Python, modules, and real-world program simulation.

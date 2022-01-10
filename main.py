from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money = MoneyMachine()

espresso = menu.find_drink("espresso")
latte = menu.find_drink("latte")
cappuccino = menu.find_drink("cappuccino")


is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}?")
    if choice == "off":
        print("Powering off...")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




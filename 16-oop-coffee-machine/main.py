from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

serve_coffee = True

while serve_coffee:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "off":
        serve_coffee = False
        print("Thank You..!!")
    elif user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        if coffee_maker.is_resource_sufficient(menu.find_drink(user_choice)):
            if money_machine.make_payment(menu.find_drink(user_choice).cost):
                coffee_maker.make_coffee(menu.find_drink(user_choice))
    else:
        print("That's not a valid option..!! \nPlease try again.")